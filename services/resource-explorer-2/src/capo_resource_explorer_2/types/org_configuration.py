"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#OrgConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resource_explorer_2.types.aws_service_access_status


class OrgConfiguration(TypedDict, closed=True):
    aws_service_access_status: "capo_resource_explorer_2.types.aws_service_access_status.AWSServiceAccessStatus"
    """<p>This value displays whether your Amazon Web Services service access is <code>ENABLED</code> or <code>DISABLED</code>.</p>"""
    service_linked_role: NotRequired["str"]
    """<p>This value shows whether or not you have a valid a service-linked role required to start the multi-account search feature.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OrgConfiguration) -> dict:
    out: dict = {}
    out["AWSServiceAccessStatus"] = value["aws_service_access_status"]
    if "service_linked_role" in value:
        out["ServiceLinkedRole"] = value["service_linked_role"]
    return out


def deserialize_json(data: dict) -> OrgConfiguration:
    out: OrgConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AWSServiceAccessStatus") is not None:
        out["aws_service_access_status"] = data["AWSServiceAccessStatus"]
    else:
        out["aws_service_access_status"] = ""
    if data.get("ServiceLinkedRole") is not None:
        out["service_linked_role"] = data["ServiceLinkedRole"]
    return out
