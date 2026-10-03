"""Generated from Smithy shape ``com.amazonaws.s3#CompletedPart``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3._protocol.xml import Element, SubElement

if TYPE_CHECKING:
    import capo_s3.types.checksum_crc32
    import capo_s3.types.checksum_crc32_c
    import capo_s3.types.checksum_crc64_nvme
    import capo_s3.types.checksum_md5
    import capo_s3.types.checksum_sha1
    import capo_s3.types.checksum_sha256
    import capo_s3.types.checksum_sha512
    import capo_s3.types.checksum_xxhash3
    import capo_s3.types.checksum_xxhash64
    import capo_s3.types.checksum_xxhash128
    import capo_s3.types.e_tag
    import capo_s3.types.part_number


class CompletedPart(TypedDict, closed=True):
    e_tag: NotRequired["capo_s3.types.e_tag.ETag"]
    """<p>Entity tag returned when the part was uploaded.</p>"""
    checksum_crc32: NotRequired["capo_s3.types.checksum_crc32.ChecksumCRC32"]
    """<p>The Base64 encoded, 32-bit <code>CRC32</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>CRC32</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc32_c: NotRequired["capo_s3.types.checksum_crc32_c.ChecksumCRC32C"]
    """<p>The Base64 encoded, 32-bit <code>CRC32C</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>CRC32C</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_crc64_nvme: NotRequired[
        "capo_s3.types.checksum_crc64_nvme.ChecksumCRC64NVME"
    ]
    """<p>The Base64 encoded, 64-bit <code>CRC64NVME</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>CRC64NVME</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha1: NotRequired["capo_s3.types.checksum_sha1.ChecksumSHA1"]
    """<p>The Base64 encoded, 160-bit <code>SHA1</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>SHA1</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha256: NotRequired["capo_s3.types.checksum_sha256.ChecksumSHA256"]
    """<p>The Base64 encoded, 256-bit <code>SHA256</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>SHA256</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_sha512: NotRequired["capo_s3.types.checksum_sha512.ChecksumSHA512"]
    """<p>The Base64 encoded, 512-bit <code>SHA512</code> digest of the part. This checksum is present if the multipart upload request was created with the <code>SHA512</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_md5: NotRequired["capo_s3.types.checksum_md5.ChecksumMD5"]
    """<p>The Base64 encoded, 128-bit <code>MD5</code> digest of the part. This checksum is present if the multipart upload request was created with the <code>MD5</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_xxhash64: NotRequired["capo_s3.types.checksum_xxhash64.ChecksumXXHASH64"]
    """<p>The Base64 encoded, 64-bit <code>XXHASH64</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>XXHASH64</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_xxhash3: NotRequired["capo_s3.types.checksum_xxhash3.ChecksumXXHASH3"]
    """<p>The Base64 encoded, 64-bit <code>XXHASH3</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>XXHASH3</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    checksum_xxhash128: NotRequired[
        "capo_s3.types.checksum_xxhash128.ChecksumXXHASH128"
    ]
    """<p>The Base64 encoded, 128-bit <code>XXHASH128</code> checksum of the part. This checksum is present if the multipart upload request was created with the <code>XXHASH128</code> checksum algorithm. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity.html">Checking object integrity</a> in the <i>Amazon S3 User Guide</i>.</p>"""
    part_number: NotRequired["capo_s3.types.part_number.PartNumber"]
    """<p>Part number that identifies the part. This is a positive integer between 1 and 10,000.</p> <note> <ul> <li> <p> <b>General purpose buckets</b> - In <code>CompleteMultipartUpload</code>, when a additional checksum (including <code>x-amz-checksum-crc32</code>, <code>x-amz-checksum-crc32c</code>, <code>x-amz-checksum-sha1</code>, or <code>x-amz-checksum-sha256</code>) is applied to each part, the <code>PartNumber</code> must start at 1 and the part numbers must be consecutive. Otherwise, Amazon S3 generates an HTTP <code>400 Bad Request</code> status code and an <code>InvalidPartOrder</code> error code.</p> </li> <li> <p> <b>Directory buckets</b> - In <code>CompleteMultipartUpload</code>, the <code>PartNumber</code> must start at 1 and the part numbers must be consecutive.</p> </li> </ul> </note>"""


# --- restXml ser/de ---
def serialize_xml(value: CompletedPart, parent: Element, tag: str) -> None:
    el = SubElement(parent, tag)
    if "e_tag" in value:
        SubElement(el, "ETag").text = str(value["e_tag"])
    if "checksum_crc32" in value:
        SubElement(el, "ChecksumCRC32").text = str(value["checksum_crc32"])
    if "checksum_crc32_c" in value:
        SubElement(el, "ChecksumCRC32C").text = str(value["checksum_crc32_c"])
    if "checksum_crc64_nvme" in value:
        SubElement(el, "ChecksumCRC64NVME").text = str(value["checksum_crc64_nvme"])
    if "checksum_sha1" in value:
        SubElement(el, "ChecksumSHA1").text = str(value["checksum_sha1"])
    if "checksum_sha256" in value:
        SubElement(el, "ChecksumSHA256").text = str(value["checksum_sha256"])
    if "checksum_sha512" in value:
        SubElement(el, "ChecksumSHA512").text = str(value["checksum_sha512"])
    if "checksum_md5" in value:
        SubElement(el, "ChecksumMD5").text = str(value["checksum_md5"])
    if "checksum_xxhash64" in value:
        SubElement(el, "ChecksumXXHASH64").text = str(value["checksum_xxhash64"])
    if "checksum_xxhash3" in value:
        SubElement(el, "ChecksumXXHASH3").text = str(value["checksum_xxhash3"])
    if "checksum_xxhash128" in value:
        SubElement(el, "ChecksumXXHASH128").text = str(value["checksum_xxhash128"])
    if "part_number" in value:
        SubElement(el, "PartNumber").text = str(value["part_number"])


def deserialize_xml(el: Element) -> CompletedPart:
    out: CompletedPart = {}  # type: ignore[typeddict-item]
    child_e_tag = el.find("ETag")
    if child_e_tag is not None:
        out["e_tag"] = str(child_e_tag.text or "")
    child_checksum_crc32 = el.find("ChecksumCRC32")
    if child_checksum_crc32 is not None:
        out["checksum_crc32"] = str(child_checksum_crc32.text or "")
    child_checksum_crc32_c = el.find("ChecksumCRC32C")
    if child_checksum_crc32_c is not None:
        out["checksum_crc32_c"] = str(child_checksum_crc32_c.text or "")
    child_checksum_crc64_nvme = el.find("ChecksumCRC64NVME")
    if child_checksum_crc64_nvme is not None:
        out["checksum_crc64_nvme"] = str(child_checksum_crc64_nvme.text or "")
    child_checksum_sha1 = el.find("ChecksumSHA1")
    if child_checksum_sha1 is not None:
        out["checksum_sha1"] = str(child_checksum_sha1.text or "")
    child_checksum_sha256 = el.find("ChecksumSHA256")
    if child_checksum_sha256 is not None:
        out["checksum_sha256"] = str(child_checksum_sha256.text or "")
    child_checksum_sha512 = el.find("ChecksumSHA512")
    if child_checksum_sha512 is not None:
        out["checksum_sha512"] = str(child_checksum_sha512.text or "")
    child_checksum_md5 = el.find("ChecksumMD5")
    if child_checksum_md5 is not None:
        out["checksum_md5"] = str(child_checksum_md5.text or "")
    child_checksum_xxhash64 = el.find("ChecksumXXHASH64")
    if child_checksum_xxhash64 is not None:
        out["checksum_xxhash64"] = str(child_checksum_xxhash64.text or "")
    child_checksum_xxhash3 = el.find("ChecksumXXHASH3")
    if child_checksum_xxhash3 is not None:
        out["checksum_xxhash3"] = str(child_checksum_xxhash3.text or "")
    child_checksum_xxhash128 = el.find("ChecksumXXHASH128")
    if child_checksum_xxhash128 is not None:
        out["checksum_xxhash128"] = str(child_checksum_xxhash128.text or "")
    child_part_number = el.find("PartNumber")
    if child_part_number is not None:
        out["part_number"] = int(child_part_number.text or "")
    return out
