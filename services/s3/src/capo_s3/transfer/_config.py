from dataclasses import dataclass
from typing import Any, TypedDict

from capo_s3.types.account_id import AccountId
from capo_s3.types.cache_control import CacheControl
from capo_s3.types.checksum_algorithm import ChecksumAlgorithm
from capo_s3.types.checksum_mode import ChecksumMode
from capo_s3.types.content_disposition import ContentDisposition
from capo_s3.types.content_encoding import ContentEncoding
from capo_s3.types.content_language import ContentLanguage
from capo_s3.types.content_type import ContentType
from capo_s3.types.expires import Expires
from capo_s3.types.grant_full_control import GrantFullControl
from capo_s3.types.grant_read import GrantRead
from capo_s3.types.grant_read_acp import GrantReadACP
from capo_s3.types.grant_write_acp import GrantWriteACP
from capo_s3.types.metadata import Metadata
from capo_s3.types.object_canned_acl import ObjectCannedACL
from capo_s3.types.object_lock_legal_hold_status import ObjectLockLegalHoldStatus
from capo_s3.types.object_lock_mode import ObjectLockMode
from capo_s3.types.object_lock_retain_until_date import ObjectLockRetainUntilDate
from capo_s3.types.object_version_id import ObjectVersionId
from capo_s3.types.request_payer import RequestPayer
from capo_s3.types.server_side_encryption import ServerSideEncryption
from capo_s3.types.sse_customer_algorithm import SSECustomerAlgorithm
from capo_s3.types.sse_customer_key import SSECustomerKey
from capo_s3.types.sse_customer_key_md5 import SSECustomerKeyMD5
from capo_s3.types.ssekms_encryption_context import SSEKMSEncryptionContext
from capo_s3.types.ssekms_key_id import SSEKMSKeyId
from capo_s3.types.storage_class import StorageClass
from capo_s3.types.tagging_header import TaggingHeader
from capo_s3.types.website_redirect_location import WebsiteRedirectLocation

# S3's own multipart limits. A part below the floor is rejected outright (the final part is exempt), and an upload
# that would need more than MAX_PARTS parts cannot be completed at all -- which is why ``resolved_chunksize`` grows
# the chunk rather than trusting the configured value.
MIN_PART_SIZE = 5 * 1024 * 1024
MAX_PART_SIZE = 5 * 1024**3
MAX_PARTS = 10_000
MAX_OBJECT_SIZE = MAX_PARTS * MAX_PART_SIZE


@dataclass(frozen=True, slots=True)
class TransferConfig:
    """How a transfer is split up and how much of it runs at once.

    Args:
        multipart_threshold: Size at which splitting the object starts to pay for the extra round trips. Below it,
            one request does the whole job.
        multipart_chunksize: Requested part size. Treated as a floor -- see :meth:`resolved_chunksize`.
        max_concurrency: How many parts are in flight at once. This is also what sets peak memory, roughly
            ``max_concurrency * multipart_chunksize``.
        max_attempts: Attempts per part, the first included. Parts are retried here rather than by the client
            pipeline so that every attempt rebuilds its body from the source.
    """

    multipart_threshold: int = 8 * 1024 * 1024
    multipart_chunksize: int = 8 * 1024 * 1024
    max_concurrency: int = 10
    max_attempts: int = 5

    def __post_init__(self) -> None:
        if self.multipart_threshold < 1:
            raise ValueError("multipart_threshold must be positive")
        if not MIN_PART_SIZE <= self.multipart_chunksize <= MAX_PART_SIZE:
            raise ValueError(
                f"multipart_chunksize must be between {MIN_PART_SIZE} and {MAX_PART_SIZE}, "
                f"got {self.multipart_chunksize}"
            )
        if self.max_concurrency < 1:
            raise ValueError("max_concurrency must be positive")
        if self.max_attempts < 1:
            raise ValueError("max_attempts must be positive")

    def is_multipart(self, size: int) -> bool:
        return size >= self.multipart_threshold

    def resolved_chunksize(self, size: int) -> int:
        """Keep the part count under S3's ceiling.

        The configured chunk size is a floor, not a promise: at 8 MiB a 100 GB object would need ~12800 parts, over
        the limit, so the chunk grows until the count fits.
        """
        if size < 0:
            raise ValueError("size must not be negative")
        if size > MAX_OBJECT_SIZE:
            raise ValueError(
                f"object of {size} bytes exceeds S3's maximum of {MAX_OBJECT_SIZE}"
            )
        chunk = max(self.multipart_chunksize, -(-size // MAX_PARTS))
        if chunk > MAX_PART_SIZE:
            raise ValueError(
                f"object of {size} bytes needs a part size above S3's maximum of {MAX_PART_SIZE}"
            )
        return chunk

    def part_ranges(self, size: int) -> list[tuple[int, int]]:
        """Where each part starts and how far it runs. Only the last one comes out short."""
        chunk = self.resolved_chunksize(size)
        return [(offset, min(chunk, size - offset)) for offset in range(0, size, chunk)]


class UploadExtraArgs(TypedDict, total=False):
    """Object metadata and encryption options forwarded to the upload."""

    acl: ObjectCannedACL
    cache_control: CacheControl
    checksum_algorithm: ChecksumAlgorithm
    content_disposition: ContentDisposition
    content_encoding: ContentEncoding
    content_language: ContentLanguage
    content_type: ContentType
    expected_bucket_owner: AccountId
    expires: Expires
    grant_full_control: GrantFullControl
    grant_read: GrantRead
    grant_read_acp: GrantReadACP
    grant_write_acp: GrantWriteACP
    metadata: Metadata
    object_lock_legal_hold_status: ObjectLockLegalHoldStatus
    object_lock_mode: ObjectLockMode
    object_lock_retain_until_date: ObjectLockRetainUntilDate
    request_payer: RequestPayer
    server_side_encryption: ServerSideEncryption
    sse_customer_algorithm: SSECustomerAlgorithm
    sse_customer_key: SSECustomerKey
    sse_customer_key_md5: SSECustomerKeyMD5
    ssekms_encryption_context: SSEKMSEncryptionContext
    ssekms_key_id: SSEKMSKeyId
    storage_class: StorageClass
    tagging: TaggingHeader
    website_redirect_location: WebsiteRedirectLocation


class DownloadExtraArgs(TypedDict, total=False):
    """Version selection and encryption options forwarded to the download.

    Every key is valid on both ``head_object`` and ``get_object``, so the whole dict goes to each.
    """

    checksum_mode: ChecksumMode
    expected_bucket_owner: AccountId
    request_payer: RequestPayer
    sse_customer_algorithm: SSECustomerAlgorithm
    sse_customer_key: SSECustomerKey
    sse_customer_key_md5: SSECustomerKeyMD5
    version_id: ObjectVersionId


def split_upload_args(
    extra: UploadExtraArgs | None,
) -> tuple[dict[str, Any], dict[str, Any]]:
    """Route *extra* into ``(create_multipart_upload_args, upload_part_args)``."""
    # What ``upload_part`` accepts. Everything else describes the object as a whole and belongs on
    # create_multipart_upload only -- sending e.g. content_type per part is rejected.
    part_keys = {
        "checksum_algorithm",
        "expected_bucket_owner",
        "request_payer",
        "sse_customer_algorithm",
        "sse_customer_key",
        "sse_customer_key_md5",
    }
    create: dict[str, Any] = dict(extra) if extra else {}
    part = {key: create.pop(key) for key in part_keys & create.keys()}
    return create, part
