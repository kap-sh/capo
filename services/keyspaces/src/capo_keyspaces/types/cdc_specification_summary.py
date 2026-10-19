"""Generated from Smithy shape ``com.amazonaws.keyspaces#CdcSpecificationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_keyspaces.types.cdc_status
    import capo_keyspaces.types.view_type


class CdcSpecificationSummary(TypedDict, closed=True):
    status: "capo_keyspaces.types.cdc_status.CdcStatus"
    """<p>The status of the CDC stream. Specifies if the table has a CDC stream.</p>"""
    view_type: NotRequired["capo_keyspaces.types.view_type.ViewType"]
    """<p>The view type specifies the changes Amazon Keyspaces records for each changed row in the stream. This setting can't be changed, after the stream has been created. </p> <p>The options are:</p> <ul> <li> <p> <code>NEW_AND_OLD_IMAGES</code> - both versions of the row, before and after the change. This is the default.</p> </li> <li> <p> <code>NEW_IMAGE</code> - the version of the row after the change.</p> </li> <li> <p> <code>OLD_IMAGE</code> - the version of the row before the change.</p> </li> <li> <p> <code>KEYS_ONLY</code> - the partition and clustering keys of the row that was changed.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CdcSpecificationSummary) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "view_type" in value:
        out["viewType"] = value["view_type"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CdcSpecificationSummary:
    out: CdcSpecificationSummary = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("viewType") is not None:
        out["view_type"] = data["viewType"]
    return out
