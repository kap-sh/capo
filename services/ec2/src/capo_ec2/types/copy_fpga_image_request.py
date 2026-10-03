"""Generated from Smithy shape ``com.amazonaws.ec2#CopyFpgaImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.string


class CopyFpgaImageRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    source_fpga_image_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the source AFI.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the new AFI.</p>"""
    name: NotRequired["capo_ec2.types.string.String"]
    """<p>The name for the new AFI. The default is the name of the source AFI.</p>"""
    source_region: NotRequired["capo_ec2.types.string.String"]
    """<p>The Region that contains the source AFI.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopyFpgaImageRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "source_fpga_image_id" in value:
        pairs.append(
            (f"{key_prefix}SourceFpgaImageId", str(value["source_fpga_image_id"]))
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "source_region" in value:
        pairs.append((f"{key_prefix}SourceRegion", str(value["source_region"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))


def deserialize_ec2_query(el: Element) -> CopyFpgaImageRequest:
    out: CopyFpgaImageRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_source_fpga_image_id = el.find("SourceFpgaImageId")
    if child_source_fpga_image_id is not None:
        out["source_fpga_image_id"] = str(child_source_fpga_image_id.text or "")
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_source_region = el.find("SourceRegion")
    if child_source_region is not None:
        out["source_region"] = str(child_source_region.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    return out
