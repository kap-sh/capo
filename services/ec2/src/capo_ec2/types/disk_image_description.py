"""Generated from Smithy shape ``com.amazonaws.ec2#DiskImageDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.disk_image_format
    import capo_ec2.types.import_manifest_url
    import capo_ec2.types.long
    import capo_ec2.types.string


class DiskImageDescription(TypedDict, closed=True):
    checksum: NotRequired["capo_ec2.types.string.String"]
    """<p>The checksum computed for the disk image.</p>"""
    format: NotRequired["capo_ec2.types.disk_image_format.DiskImageFormat"]
    """<p>The disk image format.</p>"""
    import_manifest_url: NotRequired[
        "capo_ec2.types.import_manifest_url.ImportManifestUrl"
    ]
    """<p>A presigned URL for the import manifest stored in Amazon S3. For information about creating a presigned URL for an Amazon S3 object, read the "Query String Request Authentication Alternative" section of the <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html">Authenticating REST Requests</a> topic in the <i>Amazon Simple Storage Service Developer Guide</i>.</p> <p>For information about the import manifest referenced by this API action, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/manifest.html">VM Import Manifest</a>.</p>"""
    size: NotRequired["capo_ec2.types.long.Long"]
    """<p>The size of the disk image, in GiB.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: DiskImageDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "checksum" in value:
        pairs.append((f"{key_prefix}Checksum", str(value["checksum"])))
    if "format" in value:
        import capo_ec2.types.disk_image_format

        capo_ec2.types.disk_image_format.serialize_ec2_query(
            value["format"], pairs, f"{key_prefix}Format"
        )
    if "import_manifest_url" in value:
        pairs.append(
            (f"{key_prefix}ImportManifestUrl", str(value["import_manifest_url"]))
        )
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))


def deserialize_ec2_query(el: Element) -> DiskImageDescription:
    out: DiskImageDescription = {}  # type: ignore[typeddict-item]
    child_checksum = el.find("checksum")
    if child_checksum is not None:
        out["checksum"] = str(child_checksum.text or "")
    child_format = el.find("format")
    if child_format is not None:
        import capo_ec2.types.disk_image_format

        out["format"] = capo_ec2.types.disk_image_format.deserialize_ec2_query(
            child_format
        )
    child_import_manifest_url = el.find("importManifestUrl")
    if child_import_manifest_url is not None:
        out["import_manifest_url"] = str(child_import_manifest_url.text or "")
    child_size = el.find("size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    return out
