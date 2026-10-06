"""Multipart upload and download. Generated from Smithy shape ``com.amazonaws.s3#AmazonS3``."""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Iterator
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING, Literal, Optional

import anyio
from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_s3.types.account_id
    import capo_s3.types.bucket_key_enabled
    import capo_s3.types.bucket_name
    import capo_s3.types.cache_control
    import capo_s3.types.checksum_algorithm
    import capo_s3.types.checksum_mode
    import capo_s3.types.complete_multipart_upload_output
    import capo_s3.types.completed_part
    import capo_s3.types.content_disposition
    import capo_s3.types.content_encoding
    import capo_s3.types.content_language
    import capo_s3.types.content_type
    import capo_s3.types.expires
    import capo_s3.types.grant_full_control
    import capo_s3.types.grant_read
    import capo_s3.types.grant_read_acp
    import capo_s3.types.grant_write_acp
    import capo_s3.types.if_match
    import capo_s3.types.if_modified_since
    import capo_s3.types.if_none_match
    import capo_s3.types.if_unmodified_since
    import capo_s3.types.metadata
    import capo_s3.types.object_canned_acl
    import capo_s3.types.object_key
    import capo_s3.types.object_lock_event_hold
    import capo_s3.types.object_lock_event_hold_duration_days
    import capo_s3.types.object_lock_event_hold_duration_years
    import capo_s3.types.object_lock_legal_hold_status
    import capo_s3.types.object_lock_mode
    import capo_s3.types.object_lock_retain_until_date
    import capo_s3.types.object_version_id
    import capo_s3.types.put_object_output
    import capo_s3.types.request_payer
    import capo_s3.types.response_cache_control
    import capo_s3.types.response_content_disposition
    import capo_s3.types.response_content_encoding
    import capo_s3.types.response_content_language
    import capo_s3.types.response_content_type
    import capo_s3.types.response_expires
    import capo_s3.types.server_side_encryption
    import capo_s3.types.sse_customer_algorithm
    import capo_s3.types.sse_customer_key
    import capo_s3.types.sse_customer_key_md5
    import capo_s3.types.ssekms_encryption_context
    import capo_s3.types.ssekms_key_id
    import capo_s3.types.storage_class
    import capo_s3.types.tagging_header
    import capo_s3.types.website_redirect_location
    from capo_s3._services.async_s3 import AsyncS3Client, AsyncS3ClientConfig
    from capo_s3._services.s3 import S3Client, S3ClientConfig


@dataclass(frozen=True, slots=True)
class Transferred:
    """Some bytes made it to S3."""

    bytes: int  # sent since the previous event
    transferred_bytes: int  # sent so far
    total_bytes: int


@dataclass(frozen=True, slots=True)
class Downloaded:
    """Some bytes arrived from S3."""

    data: bytes
    offset: int  # where `data` starts in the object
    transferred_bytes: int  # received so far, including `data`
    total_bytes: int


class TransferConfig(TypedDict, total=False, closed=True):
    target_part_size_bytes: int
    multipart_upload_threshold_bytes: int
    multipart_download_type: Literal["part", "range"]


class Upload:
    """Entering creates the upload, iterating sends the bytes, exiting completes or aborts it."""

    def __init__(
        self,
        client: S3Client,
        *,
        path: Path,
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        part_size: int,
        multipart_threshold: int,
        config_overrides: Optional[S3ClientConfig] = None,
        acl: Optional[capo_s3.types.object_canned_acl.ObjectCannedACL] = None,
        cache_control: Optional[capo_s3.types.cache_control.CacheControl] = None,
        content_disposition: Optional[
            capo_s3.types.content_disposition.ContentDisposition
        ] = None,
        content_encoding: Optional[
            capo_s3.types.content_encoding.ContentEncoding
        ] = None,
        content_language: Optional[
            capo_s3.types.content_language.ContentLanguage
        ] = None,
        content_type: Optional[capo_s3.types.content_type.ContentType] = None,
        checksum_algorithm: Optional[
            capo_s3.types.checksum_algorithm.ChecksumAlgorithm
        ] = None,
        expires: Optional[capo_s3.types.expires.Expires] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        grant_full_control: Optional[
            capo_s3.types.grant_full_control.GrantFullControl
        ] = None,
        grant_read: Optional[capo_s3.types.grant_read.GrantRead] = None,
        grant_read_acp: Optional[capo_s3.types.grant_read_acp.GrantReadACP] = None,
        grant_write_acp: Optional[capo_s3.types.grant_write_acp.GrantWriteACP] = None,
        metadata: Optional[capo_s3.types.metadata.Metadata] = None,
        server_side_encryption: Optional[
            capo_s3.types.server_side_encryption.ServerSideEncryption
        ] = None,
        storage_class: Optional[capo_s3.types.storage_class.StorageClass] = None,
        website_redirect_location: Optional[
            capo_s3.types.website_redirect_location.WebsiteRedirectLocation
        ] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        ssekms_key_id: Optional[capo_s3.types.ssekms_key_id.SSEKMSKeyId] = None,
        ssekms_encryption_context: Optional[
            capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext
        ] = None,
        bucket_key_enabled: Optional[
            capo_s3.types.bucket_key_enabled.BucketKeyEnabled
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        tagging: Optional[capo_s3.types.tagging_header.TaggingHeader] = None,
        object_lock_mode: Optional[
            capo_s3.types.object_lock_mode.ObjectLockMode
        ] = None,
        object_lock_retain_until_date: Optional[
            capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate
        ] = None,
        object_lock_legal_hold_status: Optional[
            capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus
        ] = None,
        object_lock_event_hold: Optional[
            capo_s3.types.object_lock_event_hold.ObjectLockEventHold
        ] = None,
        object_lock_event_hold_duration_days: Optional[
            capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays
        ] = None,
        object_lock_event_hold_duration_years: Optional[
            capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears
        ] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
    ):
        self._client = client
        self._path = path
        self._bucket = bucket
        self._key = key
        self._part_size = part_size
        self._multipart_threshold = multipart_threshold
        self._config_overrides = config_overrides
        self._acl = acl
        self._cache_control = cache_control
        self._content_disposition = content_disposition
        self._content_encoding = content_encoding
        self._content_language = content_language
        self._content_type = content_type
        self._checksum_algorithm = checksum_algorithm
        self._expires = expires
        self._if_match = if_match
        self._if_none_match = if_none_match
        self._grant_full_control = grant_full_control
        self._grant_read = grant_read
        self._grant_read_acp = grant_read_acp
        self._grant_write_acp = grant_write_acp
        self._metadata = metadata
        self._server_side_encryption = server_side_encryption
        self._storage_class = storage_class
        self._website_redirect_location = website_redirect_location
        self._sse_customer_algorithm = sse_customer_algorithm
        self._sse_customer_key = sse_customer_key
        self._sse_customer_key_md5 = sse_customer_key_md5
        self._ssekms_key_id = ssekms_key_id
        self._ssekms_encryption_context = ssekms_encryption_context
        self._bucket_key_enabled = bucket_key_enabled
        self._request_payer = request_payer
        self._tagging = tagging
        self._object_lock_mode = object_lock_mode
        self._object_lock_retain_until_date = object_lock_retain_until_date
        self._object_lock_legal_hold_status = object_lock_legal_hold_status
        self._object_lock_event_hold = object_lock_event_hold
        self._object_lock_event_hold_duration_days = (
            object_lock_event_hold_duration_days
        )
        self._object_lock_event_hold_duration_years = (
            object_lock_event_hold_duration_years
        )
        self._expected_bucket_owner = expected_bucket_owner
        self.total_bytes: int  # set on enter
        self._parts: list[capo_s3.types.completed_part.CompletedPart] = []
        self._all_parts_sent = False
        self.upload_id: str | None = None  # stays None for a single put_object
        # set once the upload is complete
        self.output: (
            capo_s3.types.put_object_output.PutObjectOutput
            | capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput
            | None
        ) = None

    def __enter__(self) -> Upload:
        self.total_bytes = self._path.stat().st_size
        if self.total_bytes >= self._multipart_threshold:
            created = self._client.create_multipart_upload(
                self._bucket,
                self._key,
                config_overrides=self._config_overrides,
                acl=self._acl,
                cache_control=self._cache_control,
                content_disposition=self._content_disposition,
                content_encoding=self._content_encoding,
                content_language=self._content_language,
                content_type=self._content_type,
                checksum_algorithm=self._checksum_algorithm,
                expires=self._expires,
                grant_full_control=self._grant_full_control,
                grant_read=self._grant_read,
                grant_read_acp=self._grant_read_acp,
                grant_write_acp=self._grant_write_acp,
                metadata=self._metadata,
                server_side_encryption=self._server_side_encryption,
                storage_class=self._storage_class,
                website_redirect_location=self._website_redirect_location,
                sse_customer_algorithm=self._sse_customer_algorithm,
                sse_customer_key=self._sse_customer_key,
                sse_customer_key_md5=self._sse_customer_key_md5,
                ssekms_key_id=self._ssekms_key_id,
                ssekms_encryption_context=self._ssekms_encryption_context,
                bucket_key_enabled=self._bucket_key_enabled,
                request_payer=self._request_payer,
                tagging=self._tagging,
                object_lock_mode=self._object_lock_mode,
                object_lock_retain_until_date=self._object_lock_retain_until_date,
                object_lock_legal_hold_status=self._object_lock_legal_hold_status,
                object_lock_event_hold=self._object_lock_event_hold,
                object_lock_event_hold_duration_days=self._object_lock_event_hold_duration_days,
                object_lock_event_hold_duration_years=self._object_lock_event_hold_duration_years,
                expected_bucket_owner=self._expected_bucket_owner,
            )
            assert "upload_id" in created
            self.upload_id = created["upload_id"]
        return self

    def __iter__(self) -> Iterator[Transferred]:
        if self.upload_id is None:
            self.output = self._client.put_object(
                self._bucket,
                self._key,
                body=self._path.read_bytes(),
                content_length=self.total_bytes,
                config_overrides=self._config_overrides,
                acl=self._acl,
                cache_control=self._cache_control,
                content_disposition=self._content_disposition,
                content_encoding=self._content_encoding,
                content_language=self._content_language,
                content_type=self._content_type,
                checksum_algorithm=self._checksum_algorithm,
                expires=self._expires,
                if_match=self._if_match,
                if_none_match=self._if_none_match,
                grant_full_control=self._grant_full_control,
                grant_read=self._grant_read,
                grant_read_acp=self._grant_read_acp,
                grant_write_acp=self._grant_write_acp,
                metadata=self._metadata,
                server_side_encryption=self._server_side_encryption,
                storage_class=self._storage_class,
                website_redirect_location=self._website_redirect_location,
                sse_customer_algorithm=self._sse_customer_algorithm,
                sse_customer_key=self._sse_customer_key,
                sse_customer_key_md5=self._sse_customer_key_md5,
                ssekms_key_id=self._ssekms_key_id,
                ssekms_encryption_context=self._ssekms_encryption_context,
                bucket_key_enabled=self._bucket_key_enabled,
                request_payer=self._request_payer,
                tagging=self._tagging,
                object_lock_mode=self._object_lock_mode,
                object_lock_retain_until_date=self._object_lock_retain_until_date,
                object_lock_legal_hold_status=self._object_lock_legal_hold_status,
                object_lock_event_hold=self._object_lock_event_hold,
                object_lock_event_hold_duration_days=self._object_lock_event_hold_duration_days,
                object_lock_event_hold_duration_years=self._object_lock_event_hold_duration_years,
                expected_bucket_owner=self._expected_bucket_owner,
            )
            yield Transferred(self.total_bytes, self.total_bytes, self.total_bytes)
            return

        number = 0
        transferred = 0
        with self._path.open("rb") as f:
            while chunk := f.read(self._part_size):
                number += 1
                out = self._client.upload_part(
                    self._bucket,
                    self._key,
                    number,
                    self.upload_id,
                    body=chunk,
                    content_length=len(chunk),
                    config_overrides=self._config_overrides,
                    checksum_algorithm=self._checksum_algorithm,
                    sse_customer_algorithm=self._sse_customer_algorithm,
                    sse_customer_key=self._sse_customer_key,
                    sse_customer_key_md5=self._sse_customer_key_md5,
                    request_payer=self._request_payer,
                    expected_bucket_owner=self._expected_bucket_owner,
                )
                assert "e_tag" in out
                part: capo_s3.types.completed_part.CompletedPart = {
                    "part_number": number,
                    "e_tag": out["e_tag"],
                }
                if self._checksum_algorithm is not None:
                    # the upload declared this algorithm, so S3 wants each part's checksum back
                    if "checksum_crc32" in out:
                        part["checksum_crc32"] = out["checksum_crc32"]
                    if "checksum_crc32_c" in out:
                        part["checksum_crc32_c"] = out["checksum_crc32_c"]
                    if "checksum_crc64_nvme" in out:
                        part["checksum_crc64_nvme"] = out["checksum_crc64_nvme"]
                    if "checksum_sha1" in out:
                        part["checksum_sha1"] = out["checksum_sha1"]
                    if "checksum_sha256" in out:
                        part["checksum_sha256"] = out["checksum_sha256"]
                    if "checksum_sha512" in out:
                        part["checksum_sha512"] = out["checksum_sha512"]
                    if "checksum_md5" in out:
                        part["checksum_md5"] = out["checksum_md5"]
                    if "checksum_xxhash64" in out:
                        part["checksum_xxhash64"] = out["checksum_xxhash64"]
                    if "checksum_xxhash3" in out:
                        part["checksum_xxhash3"] = out["checksum_xxhash3"]
                    if "checksum_xxhash128" in out:
                        part["checksum_xxhash128"] = out["checksum_xxhash128"]
                self._parts.append(part)
                transferred += len(chunk)
                yield Transferred(len(chunk), transferred, self.total_bytes)
        self._all_parts_sent = True

    def __exit__(self, exc_type: type[BaseException] | None, *_: object) -> None:
        if self.upload_id is None:
            return
        completed = False
        try:
            if exc_type is None and self._all_parts_sent:
                self.output = self._client.complete_multipart_upload(
                    self._bucket,
                    self._key,
                    self.upload_id,
                    multipart_upload={"parts": self._parts},
                    config_overrides=self._config_overrides,
                    if_match=self._if_match,
                    if_none_match=self._if_none_match,
                    sse_customer_algorithm=self._sse_customer_algorithm,
                    sse_customer_key=self._sse_customer_key,
                    sse_customer_key_md5=self._sse_customer_key_md5,
                    request_payer=self._request_payer,
                    expected_bucket_owner=self._expected_bucket_owner,
                )
                completed = True
        finally:
            if not completed:
                self._client.abort_multipart_upload(
                    self._bucket,
                    self._key,
                    self.upload_id,
                    config_overrides=self._config_overrides,
                    request_payer=self._request_payer,
                    expected_bucket_owner=self._expected_bucket_owner,
                )


class TransferManager:
    def __init__(
        self,
        client: S3Client,
        *,
        target_part_size_bytes: int,
        multipart_upload_threshold_bytes: int,
        multipart_download_type: Literal["part", "range"],
    ):
        self.client = client
        self.target_part_size_bytes = target_part_size_bytes
        self.multipart_upload_threshold_bytes = multipart_upload_threshold_bytes
        self.multipart_download_type: Literal["part", "range"] = multipart_download_type

    def upload_iter(
        self,
        source: str | os.PathLike[str],
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        *,
        config_overrides: Optional[S3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        acl: Optional[capo_s3.types.object_canned_acl.ObjectCannedACL] = None,
        cache_control: Optional[capo_s3.types.cache_control.CacheControl] = None,
        content_disposition: Optional[
            capo_s3.types.content_disposition.ContentDisposition
        ] = None,
        content_encoding: Optional[
            capo_s3.types.content_encoding.ContentEncoding
        ] = None,
        content_language: Optional[
            capo_s3.types.content_language.ContentLanguage
        ] = None,
        content_type: Optional[capo_s3.types.content_type.ContentType] = None,
        checksum_algorithm: Optional[
            capo_s3.types.checksum_algorithm.ChecksumAlgorithm
        ] = None,
        expires: Optional[capo_s3.types.expires.Expires] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        grant_full_control: Optional[
            capo_s3.types.grant_full_control.GrantFullControl
        ] = None,
        grant_read: Optional[capo_s3.types.grant_read.GrantRead] = None,
        grant_read_acp: Optional[capo_s3.types.grant_read_acp.GrantReadACP] = None,
        grant_write_acp: Optional[capo_s3.types.grant_write_acp.GrantWriteACP] = None,
        metadata: Optional[capo_s3.types.metadata.Metadata] = None,
        server_side_encryption: Optional[
            capo_s3.types.server_side_encryption.ServerSideEncryption
        ] = None,
        storage_class: Optional[capo_s3.types.storage_class.StorageClass] = None,
        website_redirect_location: Optional[
            capo_s3.types.website_redirect_location.WebsiteRedirectLocation
        ] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        ssekms_key_id: Optional[capo_s3.types.ssekms_key_id.SSEKMSKeyId] = None,
        ssekms_encryption_context: Optional[
            capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext
        ] = None,
        bucket_key_enabled: Optional[
            capo_s3.types.bucket_key_enabled.BucketKeyEnabled
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        tagging: Optional[capo_s3.types.tagging_header.TaggingHeader] = None,
        object_lock_mode: Optional[
            capo_s3.types.object_lock_mode.ObjectLockMode
        ] = None,
        object_lock_retain_until_date: Optional[
            capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate
        ] = None,
        object_lock_legal_hold_status: Optional[
            capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus
        ] = None,
        object_lock_event_hold: Optional[
            capo_s3.types.object_lock_event_hold.ObjectLockEventHold
        ] = None,
        object_lock_event_hold_duration_days: Optional[
            capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays
        ] = None,
        object_lock_event_hold_duration_years: Optional[
            capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears
        ] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
    ) -> Upload:
        overrides: TransferConfig = transfer_config_overrides or {}
        return Upload(
            self.client,
            path=Path(source),
            bucket=bucket,
            key=key,
            part_size=overrides.get(
                "target_part_size_bytes", self.target_part_size_bytes
            ),
            multipart_threshold=overrides.get(
                "multipart_upload_threshold_bytes",
                self.multipart_upload_threshold_bytes,
            ),
            config_overrides=config_overrides,
            acl=acl,
            cache_control=cache_control,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            checksum_algorithm=checksum_algorithm,
            expires=expires,
            if_match=if_match,
            if_none_match=if_none_match,
            grant_full_control=grant_full_control,
            grant_read=grant_read,
            grant_read_acp=grant_read_acp,
            grant_write_acp=grant_write_acp,
            metadata=metadata,
            server_side_encryption=server_side_encryption,
            storage_class=storage_class,
            website_redirect_location=website_redirect_location,
            sse_customer_algorithm=sse_customer_algorithm,
            sse_customer_key=sse_customer_key,
            sse_customer_key_md5=sse_customer_key_md5,
            ssekms_key_id=ssekms_key_id,
            ssekms_encryption_context=ssekms_encryption_context,
            bucket_key_enabled=bucket_key_enabled,
            request_payer=request_payer,
            tagging=tagging,
            object_lock_mode=object_lock_mode,
            object_lock_retain_until_date=object_lock_retain_until_date,
            object_lock_legal_hold_status=object_lock_legal_hold_status,
            object_lock_event_hold=object_lock_event_hold,
            object_lock_event_hold_duration_days=object_lock_event_hold_duration_days,
            object_lock_event_hold_duration_years=object_lock_event_hold_duration_years,
            expected_bucket_owner=expected_bucket_owner,
        )

    def upload(
        self,
        source: str | os.PathLike[str],
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        *,
        config_overrides: Optional[S3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        acl: Optional[capo_s3.types.object_canned_acl.ObjectCannedACL] = None,
        cache_control: Optional[capo_s3.types.cache_control.CacheControl] = None,
        content_disposition: Optional[
            capo_s3.types.content_disposition.ContentDisposition
        ] = None,
        content_encoding: Optional[
            capo_s3.types.content_encoding.ContentEncoding
        ] = None,
        content_language: Optional[
            capo_s3.types.content_language.ContentLanguage
        ] = None,
        content_type: Optional[capo_s3.types.content_type.ContentType] = None,
        checksum_algorithm: Optional[
            capo_s3.types.checksum_algorithm.ChecksumAlgorithm
        ] = None,
        expires: Optional[capo_s3.types.expires.Expires] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        grant_full_control: Optional[
            capo_s3.types.grant_full_control.GrantFullControl
        ] = None,
        grant_read: Optional[capo_s3.types.grant_read.GrantRead] = None,
        grant_read_acp: Optional[capo_s3.types.grant_read_acp.GrantReadACP] = None,
        grant_write_acp: Optional[capo_s3.types.grant_write_acp.GrantWriteACP] = None,
        metadata: Optional[capo_s3.types.metadata.Metadata] = None,
        server_side_encryption: Optional[
            capo_s3.types.server_side_encryption.ServerSideEncryption
        ] = None,
        storage_class: Optional[capo_s3.types.storage_class.StorageClass] = None,
        website_redirect_location: Optional[
            capo_s3.types.website_redirect_location.WebsiteRedirectLocation
        ] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        ssekms_key_id: Optional[capo_s3.types.ssekms_key_id.SSEKMSKeyId] = None,
        ssekms_encryption_context: Optional[
            capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext
        ] = None,
        bucket_key_enabled: Optional[
            capo_s3.types.bucket_key_enabled.BucketKeyEnabled
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        tagging: Optional[capo_s3.types.tagging_header.TaggingHeader] = None,
        object_lock_mode: Optional[
            capo_s3.types.object_lock_mode.ObjectLockMode
        ] = None,
        object_lock_retain_until_date: Optional[
            capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate
        ] = None,
        object_lock_legal_hold_status: Optional[
            capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus
        ] = None,
        object_lock_event_hold: Optional[
            capo_s3.types.object_lock_event_hold.ObjectLockEventHold
        ] = None,
        object_lock_event_hold_duration_days: Optional[
            capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays
        ] = None,
        object_lock_event_hold_duration_years: Optional[
            capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears
        ] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
    ) -> (
        capo_s3.types.put_object_output.PutObjectOutput
        | capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput
    ):
        with self.upload_iter(
            source,
            bucket,
            key,
            config_overrides=config_overrides,
            transfer_config_overrides=transfer_config_overrides,
            acl=acl,
            cache_control=cache_control,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            checksum_algorithm=checksum_algorithm,
            expires=expires,
            if_match=if_match,
            if_none_match=if_none_match,
            grant_full_control=grant_full_control,
            grant_read=grant_read,
            grant_read_acp=grant_read_acp,
            grant_write_acp=grant_write_acp,
            metadata=metadata,
            server_side_encryption=server_side_encryption,
            storage_class=storage_class,
            website_redirect_location=website_redirect_location,
            sse_customer_algorithm=sse_customer_algorithm,
            sse_customer_key=sse_customer_key,
            sse_customer_key_md5=sse_customer_key_md5,
            ssekms_key_id=ssekms_key_id,
            ssekms_encryption_context=ssekms_encryption_context,
            bucket_key_enabled=bucket_key_enabled,
            request_payer=request_payer,
            tagging=tagging,
            object_lock_mode=object_lock_mode,
            object_lock_retain_until_date=object_lock_retain_until_date,
            object_lock_legal_hold_status=object_lock_legal_hold_status,
            object_lock_event_hold=object_lock_event_hold,
            object_lock_event_hold_duration_days=object_lock_event_hold_duration_days,
            object_lock_event_hold_duration_years=object_lock_event_hold_duration_years,
            expected_bucket_owner=expected_bucket_owner,
        ) as upload:
            for _ in upload:
                pass
        assert upload.output is not None
        return upload.output

    def download_iter(
        self,
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        *,
        config_overrides: Optional[S3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_modified_since: Optional[
            capo_s3.types.if_modified_since.IfModifiedSince
        ] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        if_unmodified_since: Optional[
            capo_s3.types.if_unmodified_since.IfUnmodifiedSince
        ] = None,
        response_cache_control: Optional[
            capo_s3.types.response_cache_control.ResponseCacheControl
        ] = None,
        response_content_disposition: Optional[
            capo_s3.types.response_content_disposition.ResponseContentDisposition
        ] = None,
        response_content_encoding: Optional[
            capo_s3.types.response_content_encoding.ResponseContentEncoding
        ] = None,
        response_content_language: Optional[
            capo_s3.types.response_content_language.ResponseContentLanguage
        ] = None,
        response_content_type: Optional[
            capo_s3.types.response_content_type.ResponseContentType
        ] = None,
        response_expires: Optional[
            capo_s3.types.response_expires.ResponseExpires
        ] = None,
        version_id: Optional[capo_s3.types.object_version_id.ObjectVersionId] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
        checksum_mode: Optional[capo_s3.types.checksum_mode.ChecksumMode] = None,
    ) -> Iterator[Downloaded]:
        overrides: TransferConfig = transfer_config_overrides or {}
        part_size = overrides.get("target_part_size_bytes", self.target_part_size_bytes)
        download_type = overrides.get(
            "multipart_download_type", self.multipart_download_type
        )
        total: int | None = None
        e_tag = if_match
        transferred = 0
        number = 0
        while total is None or transferred < total:
            number += 1
            if download_type == "part":
                response = self.client.get_object(
                    bucket,
                    key,
                    part_number=number,
                    if_match=e_tag,
                    config_overrides=config_overrides,
                    if_modified_since=if_modified_since,
                    if_none_match=if_none_match,
                    if_unmodified_since=if_unmodified_since,
                    response_cache_control=response_cache_control,
                    response_content_disposition=response_content_disposition,
                    response_content_encoding=response_content_encoding,
                    response_content_language=response_content_language,
                    response_content_type=response_content_type,
                    response_expires=response_expires,
                    version_id=version_id,
                    sse_customer_algorithm=sse_customer_algorithm,
                    sse_customer_key=sse_customer_key,
                    sse_customer_key_md5=sse_customer_key_md5,
                    request_payer=request_payer,
                    expected_bucket_owner=expected_bucket_owner,
                    checksum_mode=checksum_mode,
                )
            else:
                end = transferred + part_size - 1
                response = self.client.get_object(
                    bucket,
                    key,
                    range=f"bytes={transferred}-{end}",
                    if_match=e_tag,
                    config_overrides=config_overrides,
                    if_modified_since=if_modified_since,
                    if_none_match=if_none_match,
                    if_unmodified_since=if_unmodified_since,
                    response_cache_control=response_cache_control,
                    response_content_disposition=response_content_disposition,
                    response_content_encoding=response_content_encoding,
                    response_content_language=response_content_language,
                    response_content_type=response_content_type,
                    response_expires=response_expires,
                    version_id=version_id,
                    sse_customer_algorithm=sse_customer_algorithm,
                    sse_customer_key=sse_customer_key,
                    sse_customer_key_md5=sse_customer_key_md5,
                    request_payer=request_payer,
                    expected_bucket_owner=expected_bucket_owner,
                    checksum_mode=checksum_mode,
                )
            with response as out:
                if total is None:
                    # later requests are pinned to the first response's ETag
                    e_tag = out["e_tag"] if "e_tag" in out else None
                    if "content_length" in out and out["content_length"] == 0:
                        total = 0
                    else:
                        assert "content_range" in out
                        total = int(out["content_range"].rsplit("/", 1)[1])
                for chunk in out["body"]:
                    offset = transferred
                    transferred += len(chunk)
                    yield Downloaded(chunk, offset, transferred, total)

    def download(
        self,
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        destination: str | os.PathLike[str],
        *,
        config_overrides: Optional[S3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_modified_since: Optional[
            capo_s3.types.if_modified_since.IfModifiedSince
        ] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        if_unmodified_since: Optional[
            capo_s3.types.if_unmodified_since.IfUnmodifiedSince
        ] = None,
        response_cache_control: Optional[
            capo_s3.types.response_cache_control.ResponseCacheControl
        ] = None,
        response_content_disposition: Optional[
            capo_s3.types.response_content_disposition.ResponseContentDisposition
        ] = None,
        response_content_encoding: Optional[
            capo_s3.types.response_content_encoding.ResponseContentEncoding
        ] = None,
        response_content_language: Optional[
            capo_s3.types.response_content_language.ResponseContentLanguage
        ] = None,
        response_content_type: Optional[
            capo_s3.types.response_content_type.ResponseContentType
        ] = None,
        response_expires: Optional[
            capo_s3.types.response_expires.ResponseExpires
        ] = None,
        version_id: Optional[capo_s3.types.object_version_id.ObjectVersionId] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
        checksum_mode: Optional[capo_s3.types.checksum_mode.ChecksumMode] = None,
    ) -> None:
        with open(destination, "wb") as f:
            for event in self.download_iter(
                bucket,
                key,
                config_overrides=config_overrides,
                transfer_config_overrides=transfer_config_overrides,
                if_match=if_match,
                if_modified_since=if_modified_since,
                if_none_match=if_none_match,
                if_unmodified_since=if_unmodified_since,
                response_cache_control=response_cache_control,
                response_content_disposition=response_content_disposition,
                response_content_encoding=response_content_encoding,
                response_content_language=response_content_language,
                response_content_type=response_content_type,
                response_expires=response_expires,
                version_id=version_id,
                sse_customer_algorithm=sse_customer_algorithm,
                sse_customer_key=sse_customer_key,
                sse_customer_key_md5=sse_customer_key_md5,
                request_payer=request_payer,
                expected_bucket_owner=expected_bucket_owner,
                checksum_mode=checksum_mode,
            ):
                f.seek(event.offset)
                f.write(event.data)


class AsyncUpload:
    """Entering creates the upload, iterating sends the bytes, exiting completes or aborts it."""

    def __init__(
        self,
        client: AsyncS3Client,
        *,
        path: anyio.Path,
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        part_size: int,
        multipart_threshold: int,
        config_overrides: Optional[AsyncS3ClientConfig] = None,
        acl: Optional[capo_s3.types.object_canned_acl.ObjectCannedACL] = None,
        cache_control: Optional[capo_s3.types.cache_control.CacheControl] = None,
        content_disposition: Optional[
            capo_s3.types.content_disposition.ContentDisposition
        ] = None,
        content_encoding: Optional[
            capo_s3.types.content_encoding.ContentEncoding
        ] = None,
        content_language: Optional[
            capo_s3.types.content_language.ContentLanguage
        ] = None,
        content_type: Optional[capo_s3.types.content_type.ContentType] = None,
        checksum_algorithm: Optional[
            capo_s3.types.checksum_algorithm.ChecksumAlgorithm
        ] = None,
        expires: Optional[capo_s3.types.expires.Expires] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        grant_full_control: Optional[
            capo_s3.types.grant_full_control.GrantFullControl
        ] = None,
        grant_read: Optional[capo_s3.types.grant_read.GrantRead] = None,
        grant_read_acp: Optional[capo_s3.types.grant_read_acp.GrantReadACP] = None,
        grant_write_acp: Optional[capo_s3.types.grant_write_acp.GrantWriteACP] = None,
        metadata: Optional[capo_s3.types.metadata.Metadata] = None,
        server_side_encryption: Optional[
            capo_s3.types.server_side_encryption.ServerSideEncryption
        ] = None,
        storage_class: Optional[capo_s3.types.storage_class.StorageClass] = None,
        website_redirect_location: Optional[
            capo_s3.types.website_redirect_location.WebsiteRedirectLocation
        ] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        ssekms_key_id: Optional[capo_s3.types.ssekms_key_id.SSEKMSKeyId] = None,
        ssekms_encryption_context: Optional[
            capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext
        ] = None,
        bucket_key_enabled: Optional[
            capo_s3.types.bucket_key_enabled.BucketKeyEnabled
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        tagging: Optional[capo_s3.types.tagging_header.TaggingHeader] = None,
        object_lock_mode: Optional[
            capo_s3.types.object_lock_mode.ObjectLockMode
        ] = None,
        object_lock_retain_until_date: Optional[
            capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate
        ] = None,
        object_lock_legal_hold_status: Optional[
            capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus
        ] = None,
        object_lock_event_hold: Optional[
            capo_s3.types.object_lock_event_hold.ObjectLockEventHold
        ] = None,
        object_lock_event_hold_duration_days: Optional[
            capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays
        ] = None,
        object_lock_event_hold_duration_years: Optional[
            capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears
        ] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
    ):
        self._client = client
        self._path = path
        self._bucket = bucket
        self._key = key
        self._part_size = part_size
        self._multipart_threshold = multipart_threshold
        self._config_overrides = config_overrides
        self._acl = acl
        self._cache_control = cache_control
        self._content_disposition = content_disposition
        self._content_encoding = content_encoding
        self._content_language = content_language
        self._content_type = content_type
        self._checksum_algorithm = checksum_algorithm
        self._expires = expires
        self._if_match = if_match
        self._if_none_match = if_none_match
        self._grant_full_control = grant_full_control
        self._grant_read = grant_read
        self._grant_read_acp = grant_read_acp
        self._grant_write_acp = grant_write_acp
        self._metadata = metadata
        self._server_side_encryption = server_side_encryption
        self._storage_class = storage_class
        self._website_redirect_location = website_redirect_location
        self._sse_customer_algorithm = sse_customer_algorithm
        self._sse_customer_key = sse_customer_key
        self._sse_customer_key_md5 = sse_customer_key_md5
        self._ssekms_key_id = ssekms_key_id
        self._ssekms_encryption_context = ssekms_encryption_context
        self._bucket_key_enabled = bucket_key_enabled
        self._request_payer = request_payer
        self._tagging = tagging
        self._object_lock_mode = object_lock_mode
        self._object_lock_retain_until_date = object_lock_retain_until_date
        self._object_lock_legal_hold_status = object_lock_legal_hold_status
        self._object_lock_event_hold = object_lock_event_hold
        self._object_lock_event_hold_duration_days = (
            object_lock_event_hold_duration_days
        )
        self._object_lock_event_hold_duration_years = (
            object_lock_event_hold_duration_years
        )
        self._expected_bucket_owner = expected_bucket_owner
        self.total_bytes: int  # set on enter
        self._parts: list[capo_s3.types.completed_part.CompletedPart] = []
        self._all_parts_sent = False
        self.upload_id: str | None = None  # stays None for a single put_object
        # set once the upload is complete
        self.output: (
            capo_s3.types.put_object_output.PutObjectOutput
            | capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput
            | None
        ) = None

    async def __aenter__(self) -> AsyncUpload:
        self.total_bytes = (await self._path.stat()).st_size
        if self.total_bytes >= self._multipart_threshold:
            created = await self._client.create_multipart_upload(
                self._bucket,
                self._key,
                config_overrides=self._config_overrides,
                acl=self._acl,
                cache_control=self._cache_control,
                content_disposition=self._content_disposition,
                content_encoding=self._content_encoding,
                content_language=self._content_language,
                content_type=self._content_type,
                checksum_algorithm=self._checksum_algorithm,
                expires=self._expires,
                grant_full_control=self._grant_full_control,
                grant_read=self._grant_read,
                grant_read_acp=self._grant_read_acp,
                grant_write_acp=self._grant_write_acp,
                metadata=self._metadata,
                server_side_encryption=self._server_side_encryption,
                storage_class=self._storage_class,
                website_redirect_location=self._website_redirect_location,
                sse_customer_algorithm=self._sse_customer_algorithm,
                sse_customer_key=self._sse_customer_key,
                sse_customer_key_md5=self._sse_customer_key_md5,
                ssekms_key_id=self._ssekms_key_id,
                ssekms_encryption_context=self._ssekms_encryption_context,
                bucket_key_enabled=self._bucket_key_enabled,
                request_payer=self._request_payer,
                tagging=self._tagging,
                object_lock_mode=self._object_lock_mode,
                object_lock_retain_until_date=self._object_lock_retain_until_date,
                object_lock_legal_hold_status=self._object_lock_legal_hold_status,
                object_lock_event_hold=self._object_lock_event_hold,
                object_lock_event_hold_duration_days=self._object_lock_event_hold_duration_days,
                object_lock_event_hold_duration_years=self._object_lock_event_hold_duration_years,
                expected_bucket_owner=self._expected_bucket_owner,
            )
            assert "upload_id" in created
            self.upload_id = created["upload_id"]
        return self

    async def __aiter__(self) -> AsyncIterator[Transferred]:
        if self.upload_id is None:
            self.output = await self._client.put_object(
                self._bucket,
                self._key,
                body=await self._path.read_bytes(),
                content_length=self.total_bytes,
                config_overrides=self._config_overrides,
                acl=self._acl,
                cache_control=self._cache_control,
                content_disposition=self._content_disposition,
                content_encoding=self._content_encoding,
                content_language=self._content_language,
                content_type=self._content_type,
                checksum_algorithm=self._checksum_algorithm,
                expires=self._expires,
                if_match=self._if_match,
                if_none_match=self._if_none_match,
                grant_full_control=self._grant_full_control,
                grant_read=self._grant_read,
                grant_read_acp=self._grant_read_acp,
                grant_write_acp=self._grant_write_acp,
                metadata=self._metadata,
                server_side_encryption=self._server_side_encryption,
                storage_class=self._storage_class,
                website_redirect_location=self._website_redirect_location,
                sse_customer_algorithm=self._sse_customer_algorithm,
                sse_customer_key=self._sse_customer_key,
                sse_customer_key_md5=self._sse_customer_key_md5,
                ssekms_key_id=self._ssekms_key_id,
                ssekms_encryption_context=self._ssekms_encryption_context,
                bucket_key_enabled=self._bucket_key_enabled,
                request_payer=self._request_payer,
                tagging=self._tagging,
                object_lock_mode=self._object_lock_mode,
                object_lock_retain_until_date=self._object_lock_retain_until_date,
                object_lock_legal_hold_status=self._object_lock_legal_hold_status,
                object_lock_event_hold=self._object_lock_event_hold,
                object_lock_event_hold_duration_days=self._object_lock_event_hold_duration_days,
                object_lock_event_hold_duration_years=self._object_lock_event_hold_duration_years,
                expected_bucket_owner=self._expected_bucket_owner,
            )
            yield Transferred(self.total_bytes, self.total_bytes, self.total_bytes)
            return

        number = 0
        transferred = 0
        async with await self._path.open("rb") as f:
            while chunk := await f.read(self._part_size):
                number += 1
                out = await self._client.upload_part(
                    self._bucket,
                    self._key,
                    number,
                    self.upload_id,
                    body=chunk,
                    content_length=len(chunk),
                    config_overrides=self._config_overrides,
                    checksum_algorithm=self._checksum_algorithm,
                    sse_customer_algorithm=self._sse_customer_algorithm,
                    sse_customer_key=self._sse_customer_key,
                    sse_customer_key_md5=self._sse_customer_key_md5,
                    request_payer=self._request_payer,
                    expected_bucket_owner=self._expected_bucket_owner,
                )
                assert "e_tag" in out
                part: capo_s3.types.completed_part.CompletedPart = {
                    "part_number": number,
                    "e_tag": out["e_tag"],
                }
                if self._checksum_algorithm is not None:
                    # the upload declared this algorithm, so S3 wants each part's checksum back
                    if "checksum_crc32" in out:
                        part["checksum_crc32"] = out["checksum_crc32"]
                    if "checksum_crc32_c" in out:
                        part["checksum_crc32_c"] = out["checksum_crc32_c"]
                    if "checksum_crc64_nvme" in out:
                        part["checksum_crc64_nvme"] = out["checksum_crc64_nvme"]
                    if "checksum_sha1" in out:
                        part["checksum_sha1"] = out["checksum_sha1"]
                    if "checksum_sha256" in out:
                        part["checksum_sha256"] = out["checksum_sha256"]
                    if "checksum_sha512" in out:
                        part["checksum_sha512"] = out["checksum_sha512"]
                    if "checksum_md5" in out:
                        part["checksum_md5"] = out["checksum_md5"]
                    if "checksum_xxhash64" in out:
                        part["checksum_xxhash64"] = out["checksum_xxhash64"]
                    if "checksum_xxhash3" in out:
                        part["checksum_xxhash3"] = out["checksum_xxhash3"]
                    if "checksum_xxhash128" in out:
                        part["checksum_xxhash128"] = out["checksum_xxhash128"]
                self._parts.append(part)
                transferred += len(chunk)
                yield Transferred(len(chunk), transferred, self.total_bytes)
        self._all_parts_sent = True

    async def __aexit__(self, exc_type: type[BaseException] | None, *_: object) -> None:
        if self.upload_id is None:
            return
        completed = False
        try:
            if exc_type is None and self._all_parts_sent:
                self.output = await self._client.complete_multipart_upload(
                    self._bucket,
                    self._key,
                    self.upload_id,
                    multipart_upload={"parts": self._parts},
                    config_overrides=self._config_overrides,
                    if_match=self._if_match,
                    if_none_match=self._if_none_match,
                    sse_customer_algorithm=self._sse_customer_algorithm,
                    sse_customer_key=self._sse_customer_key,
                    sse_customer_key_md5=self._sse_customer_key_md5,
                    request_payer=self._request_payer,
                    expected_bucket_owner=self._expected_bucket_owner,
                )
                completed = True
        finally:
            if not completed:
                await self._client.abort_multipart_upload(
                    self._bucket,
                    self._key,
                    self.upload_id,
                    config_overrides=self._config_overrides,
                    request_payer=self._request_payer,
                    expected_bucket_owner=self._expected_bucket_owner,
                )


class AsyncTransferManager:
    def __init__(
        self,
        client: AsyncS3Client,
        *,
        target_part_size_bytes: int,
        multipart_upload_threshold_bytes: int,
        multipart_download_type: Literal["part", "range"],
    ):
        self.client = client
        self.target_part_size_bytes = target_part_size_bytes
        self.multipart_upload_threshold_bytes = multipart_upload_threshold_bytes
        self.multipart_download_type: Literal["part", "range"] = multipart_download_type

    def upload_iter(
        self,
        source: str | os.PathLike[str],
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        *,
        config_overrides: Optional[AsyncS3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        acl: Optional[capo_s3.types.object_canned_acl.ObjectCannedACL] = None,
        cache_control: Optional[capo_s3.types.cache_control.CacheControl] = None,
        content_disposition: Optional[
            capo_s3.types.content_disposition.ContentDisposition
        ] = None,
        content_encoding: Optional[
            capo_s3.types.content_encoding.ContentEncoding
        ] = None,
        content_language: Optional[
            capo_s3.types.content_language.ContentLanguage
        ] = None,
        content_type: Optional[capo_s3.types.content_type.ContentType] = None,
        checksum_algorithm: Optional[
            capo_s3.types.checksum_algorithm.ChecksumAlgorithm
        ] = None,
        expires: Optional[capo_s3.types.expires.Expires] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        grant_full_control: Optional[
            capo_s3.types.grant_full_control.GrantFullControl
        ] = None,
        grant_read: Optional[capo_s3.types.grant_read.GrantRead] = None,
        grant_read_acp: Optional[capo_s3.types.grant_read_acp.GrantReadACP] = None,
        grant_write_acp: Optional[capo_s3.types.grant_write_acp.GrantWriteACP] = None,
        metadata: Optional[capo_s3.types.metadata.Metadata] = None,
        server_side_encryption: Optional[
            capo_s3.types.server_side_encryption.ServerSideEncryption
        ] = None,
        storage_class: Optional[capo_s3.types.storage_class.StorageClass] = None,
        website_redirect_location: Optional[
            capo_s3.types.website_redirect_location.WebsiteRedirectLocation
        ] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        ssekms_key_id: Optional[capo_s3.types.ssekms_key_id.SSEKMSKeyId] = None,
        ssekms_encryption_context: Optional[
            capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext
        ] = None,
        bucket_key_enabled: Optional[
            capo_s3.types.bucket_key_enabled.BucketKeyEnabled
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        tagging: Optional[capo_s3.types.tagging_header.TaggingHeader] = None,
        object_lock_mode: Optional[
            capo_s3.types.object_lock_mode.ObjectLockMode
        ] = None,
        object_lock_retain_until_date: Optional[
            capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate
        ] = None,
        object_lock_legal_hold_status: Optional[
            capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus
        ] = None,
        object_lock_event_hold: Optional[
            capo_s3.types.object_lock_event_hold.ObjectLockEventHold
        ] = None,
        object_lock_event_hold_duration_days: Optional[
            capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays
        ] = None,
        object_lock_event_hold_duration_years: Optional[
            capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears
        ] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
    ) -> AsyncUpload:
        overrides: TransferConfig = transfer_config_overrides or {}
        return AsyncUpload(
            self.client,
            path=anyio.Path(source),
            bucket=bucket,
            key=key,
            part_size=overrides.get(
                "target_part_size_bytes", self.target_part_size_bytes
            ),
            multipart_threshold=overrides.get(
                "multipart_upload_threshold_bytes",
                self.multipart_upload_threshold_bytes,
            ),
            config_overrides=config_overrides,
            acl=acl,
            cache_control=cache_control,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            checksum_algorithm=checksum_algorithm,
            expires=expires,
            if_match=if_match,
            if_none_match=if_none_match,
            grant_full_control=grant_full_control,
            grant_read=grant_read,
            grant_read_acp=grant_read_acp,
            grant_write_acp=grant_write_acp,
            metadata=metadata,
            server_side_encryption=server_side_encryption,
            storage_class=storage_class,
            website_redirect_location=website_redirect_location,
            sse_customer_algorithm=sse_customer_algorithm,
            sse_customer_key=sse_customer_key,
            sse_customer_key_md5=sse_customer_key_md5,
            ssekms_key_id=ssekms_key_id,
            ssekms_encryption_context=ssekms_encryption_context,
            bucket_key_enabled=bucket_key_enabled,
            request_payer=request_payer,
            tagging=tagging,
            object_lock_mode=object_lock_mode,
            object_lock_retain_until_date=object_lock_retain_until_date,
            object_lock_legal_hold_status=object_lock_legal_hold_status,
            object_lock_event_hold=object_lock_event_hold,
            object_lock_event_hold_duration_days=object_lock_event_hold_duration_days,
            object_lock_event_hold_duration_years=object_lock_event_hold_duration_years,
            expected_bucket_owner=expected_bucket_owner,
        )

    async def upload(
        self,
        source: str | os.PathLike[str],
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        *,
        config_overrides: Optional[AsyncS3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        acl: Optional[capo_s3.types.object_canned_acl.ObjectCannedACL] = None,
        cache_control: Optional[capo_s3.types.cache_control.CacheControl] = None,
        content_disposition: Optional[
            capo_s3.types.content_disposition.ContentDisposition
        ] = None,
        content_encoding: Optional[
            capo_s3.types.content_encoding.ContentEncoding
        ] = None,
        content_language: Optional[
            capo_s3.types.content_language.ContentLanguage
        ] = None,
        content_type: Optional[capo_s3.types.content_type.ContentType] = None,
        checksum_algorithm: Optional[
            capo_s3.types.checksum_algorithm.ChecksumAlgorithm
        ] = None,
        expires: Optional[capo_s3.types.expires.Expires] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        grant_full_control: Optional[
            capo_s3.types.grant_full_control.GrantFullControl
        ] = None,
        grant_read: Optional[capo_s3.types.grant_read.GrantRead] = None,
        grant_read_acp: Optional[capo_s3.types.grant_read_acp.GrantReadACP] = None,
        grant_write_acp: Optional[capo_s3.types.grant_write_acp.GrantWriteACP] = None,
        metadata: Optional[capo_s3.types.metadata.Metadata] = None,
        server_side_encryption: Optional[
            capo_s3.types.server_side_encryption.ServerSideEncryption
        ] = None,
        storage_class: Optional[capo_s3.types.storage_class.StorageClass] = None,
        website_redirect_location: Optional[
            capo_s3.types.website_redirect_location.WebsiteRedirectLocation
        ] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        ssekms_key_id: Optional[capo_s3.types.ssekms_key_id.SSEKMSKeyId] = None,
        ssekms_encryption_context: Optional[
            capo_s3.types.ssekms_encryption_context.SSEKMSEncryptionContext
        ] = None,
        bucket_key_enabled: Optional[
            capo_s3.types.bucket_key_enabled.BucketKeyEnabled
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        tagging: Optional[capo_s3.types.tagging_header.TaggingHeader] = None,
        object_lock_mode: Optional[
            capo_s3.types.object_lock_mode.ObjectLockMode
        ] = None,
        object_lock_retain_until_date: Optional[
            capo_s3.types.object_lock_retain_until_date.ObjectLockRetainUntilDate
        ] = None,
        object_lock_legal_hold_status: Optional[
            capo_s3.types.object_lock_legal_hold_status.ObjectLockLegalHoldStatus
        ] = None,
        object_lock_event_hold: Optional[
            capo_s3.types.object_lock_event_hold.ObjectLockEventHold
        ] = None,
        object_lock_event_hold_duration_days: Optional[
            capo_s3.types.object_lock_event_hold_duration_days.ObjectLockEventHoldDurationDays
        ] = None,
        object_lock_event_hold_duration_years: Optional[
            capo_s3.types.object_lock_event_hold_duration_years.ObjectLockEventHoldDurationYears
        ] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
    ) -> (
        capo_s3.types.put_object_output.PutObjectOutput
        | capo_s3.types.complete_multipart_upload_output.CompleteMultipartUploadOutput
    ):
        async with self.upload_iter(
            source,
            bucket,
            key,
            config_overrides=config_overrides,
            transfer_config_overrides=transfer_config_overrides,
            acl=acl,
            cache_control=cache_control,
            content_disposition=content_disposition,
            content_encoding=content_encoding,
            content_language=content_language,
            content_type=content_type,
            checksum_algorithm=checksum_algorithm,
            expires=expires,
            if_match=if_match,
            if_none_match=if_none_match,
            grant_full_control=grant_full_control,
            grant_read=grant_read,
            grant_read_acp=grant_read_acp,
            grant_write_acp=grant_write_acp,
            metadata=metadata,
            server_side_encryption=server_side_encryption,
            storage_class=storage_class,
            website_redirect_location=website_redirect_location,
            sse_customer_algorithm=sse_customer_algorithm,
            sse_customer_key=sse_customer_key,
            sse_customer_key_md5=sse_customer_key_md5,
            ssekms_key_id=ssekms_key_id,
            ssekms_encryption_context=ssekms_encryption_context,
            bucket_key_enabled=bucket_key_enabled,
            request_payer=request_payer,
            tagging=tagging,
            object_lock_mode=object_lock_mode,
            object_lock_retain_until_date=object_lock_retain_until_date,
            object_lock_legal_hold_status=object_lock_legal_hold_status,
            object_lock_event_hold=object_lock_event_hold,
            object_lock_event_hold_duration_days=object_lock_event_hold_duration_days,
            object_lock_event_hold_duration_years=object_lock_event_hold_duration_years,
            expected_bucket_owner=expected_bucket_owner,
        ) as upload:
            async for _ in upload:
                pass
        assert upload.output is not None
        return upload.output

    async def download_iter(
        self,
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        *,
        config_overrides: Optional[AsyncS3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_modified_since: Optional[
            capo_s3.types.if_modified_since.IfModifiedSince
        ] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        if_unmodified_since: Optional[
            capo_s3.types.if_unmodified_since.IfUnmodifiedSince
        ] = None,
        response_cache_control: Optional[
            capo_s3.types.response_cache_control.ResponseCacheControl
        ] = None,
        response_content_disposition: Optional[
            capo_s3.types.response_content_disposition.ResponseContentDisposition
        ] = None,
        response_content_encoding: Optional[
            capo_s3.types.response_content_encoding.ResponseContentEncoding
        ] = None,
        response_content_language: Optional[
            capo_s3.types.response_content_language.ResponseContentLanguage
        ] = None,
        response_content_type: Optional[
            capo_s3.types.response_content_type.ResponseContentType
        ] = None,
        response_expires: Optional[
            capo_s3.types.response_expires.ResponseExpires
        ] = None,
        version_id: Optional[capo_s3.types.object_version_id.ObjectVersionId] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
        checksum_mode: Optional[capo_s3.types.checksum_mode.ChecksumMode] = None,
    ) -> AsyncIterator[Downloaded]:
        overrides: TransferConfig = transfer_config_overrides or {}
        part_size = overrides.get("target_part_size_bytes", self.target_part_size_bytes)
        download_type = overrides.get(
            "multipart_download_type", self.multipart_download_type
        )
        total: int | None = None
        e_tag = if_match
        transferred = 0
        number = 0
        while total is None or transferred < total:
            number += 1
            if download_type == "part":
                response = self.client.get_object(
                    bucket,
                    key,
                    part_number=number,
                    if_match=e_tag,
                    config_overrides=config_overrides,
                    if_modified_since=if_modified_since,
                    if_none_match=if_none_match,
                    if_unmodified_since=if_unmodified_since,
                    response_cache_control=response_cache_control,
                    response_content_disposition=response_content_disposition,
                    response_content_encoding=response_content_encoding,
                    response_content_language=response_content_language,
                    response_content_type=response_content_type,
                    response_expires=response_expires,
                    version_id=version_id,
                    sse_customer_algorithm=sse_customer_algorithm,
                    sse_customer_key=sse_customer_key,
                    sse_customer_key_md5=sse_customer_key_md5,
                    request_payer=request_payer,
                    expected_bucket_owner=expected_bucket_owner,
                    checksum_mode=checksum_mode,
                )
            else:
                end = transferred + part_size - 1
                response = self.client.get_object(
                    bucket,
                    key,
                    range=f"bytes={transferred}-{end}",
                    if_match=e_tag,
                    config_overrides=config_overrides,
                    if_modified_since=if_modified_since,
                    if_none_match=if_none_match,
                    if_unmodified_since=if_unmodified_since,
                    response_cache_control=response_cache_control,
                    response_content_disposition=response_content_disposition,
                    response_content_encoding=response_content_encoding,
                    response_content_language=response_content_language,
                    response_content_type=response_content_type,
                    response_expires=response_expires,
                    version_id=version_id,
                    sse_customer_algorithm=sse_customer_algorithm,
                    sse_customer_key=sse_customer_key,
                    sse_customer_key_md5=sse_customer_key_md5,
                    request_payer=request_payer,
                    expected_bucket_owner=expected_bucket_owner,
                    checksum_mode=checksum_mode,
                )
            async with response as out:
                if total is None:
                    # later requests are pinned to the first response's ETag
                    e_tag = out["e_tag"] if "e_tag" in out else None
                    if "content_length" in out and out["content_length"] == 0:
                        total = 0
                    else:
                        assert "content_range" in out
                        total = int(out["content_range"].rsplit("/", 1)[1])
                async for chunk in out["body"]:
                    offset = transferred
                    transferred += len(chunk)
                    yield Downloaded(chunk, offset, transferred, total)

    async def download(
        self,
        bucket: capo_s3.types.bucket_name.BucketName,
        key: capo_s3.types.object_key.ObjectKey,
        destination: str | os.PathLike[str],
        *,
        config_overrides: Optional[AsyncS3ClientConfig] = None,
        transfer_config_overrides: Optional[TransferConfig] = None,
        if_match: Optional[capo_s3.types.if_match.IfMatch] = None,
        if_modified_since: Optional[
            capo_s3.types.if_modified_since.IfModifiedSince
        ] = None,
        if_none_match: Optional[capo_s3.types.if_none_match.IfNoneMatch] = None,
        if_unmodified_since: Optional[
            capo_s3.types.if_unmodified_since.IfUnmodifiedSince
        ] = None,
        response_cache_control: Optional[
            capo_s3.types.response_cache_control.ResponseCacheControl
        ] = None,
        response_content_disposition: Optional[
            capo_s3.types.response_content_disposition.ResponseContentDisposition
        ] = None,
        response_content_encoding: Optional[
            capo_s3.types.response_content_encoding.ResponseContentEncoding
        ] = None,
        response_content_language: Optional[
            capo_s3.types.response_content_language.ResponseContentLanguage
        ] = None,
        response_content_type: Optional[
            capo_s3.types.response_content_type.ResponseContentType
        ] = None,
        response_expires: Optional[
            capo_s3.types.response_expires.ResponseExpires
        ] = None,
        version_id: Optional[capo_s3.types.object_version_id.ObjectVersionId] = None,
        sse_customer_algorithm: Optional[
            capo_s3.types.sse_customer_algorithm.SSECustomerAlgorithm
        ] = None,
        sse_customer_key: Optional[
            capo_s3.types.sse_customer_key.SSECustomerKey
        ] = None,
        sse_customer_key_md5: Optional[
            capo_s3.types.sse_customer_key_md5.SSECustomerKeyMD5
        ] = None,
        request_payer: Optional[capo_s3.types.request_payer.RequestPayer] = None,
        expected_bucket_owner: Optional[capo_s3.types.account_id.AccountId] = None,
        checksum_mode: Optional[capo_s3.types.checksum_mode.ChecksumMode] = None,
    ) -> None:
        async with await anyio.open_file(destination, "wb") as f:
            async for event in self.download_iter(
                bucket,
                key,
                config_overrides=config_overrides,
                transfer_config_overrides=transfer_config_overrides,
                if_match=if_match,
                if_modified_since=if_modified_since,
                if_none_match=if_none_match,
                if_unmodified_since=if_unmodified_since,
                response_cache_control=response_cache_control,
                response_content_disposition=response_content_disposition,
                response_content_encoding=response_content_encoding,
                response_content_language=response_content_language,
                response_content_type=response_content_type,
                response_expires=response_expires,
                version_id=version_id,
                sse_customer_algorithm=sse_customer_algorithm,
                sse_customer_key=sse_customer_key,
                sse_customer_key_md5=sse_customer_key_md5,
                request_payer=request_payer,
                expected_bucket_owner=expected_bucket_owner,
                checksum_mode=checksum_mode,
            ):
                await f.seek(event.offset)
                await f.write(event.data)
