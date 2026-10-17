"""Generated from Smithy shape ``com.amazonaws.connect#DescribeContactFlowAliasResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_flow_alias_info


class DescribeContactFlowAliasResponse(TypedDict, closed=True):
    contact_flow_alias: NotRequired[
        "capo_connect.types.contact_flow_alias_info.ContactFlowAliasInfo"
    ]
    """<p>Information about the flow alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeContactFlowAliasResponse) -> dict:
    out: dict = {}
    if "contact_flow_alias" in value:
        import capo_connect.types.contact_flow_alias_info

        out["ContactFlowAlias"] = (
            capo_connect.types.contact_flow_alias_info.serialize_json(
                value["contact_flow_alias"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeContactFlowAliasResponse:
    out: DescribeContactFlowAliasResponse = {}  # type: ignore[typeddict-item]
    if data.get("ContactFlowAlias") is not None:
        import capo_connect.types.contact_flow_alias_info

        out["contact_flow_alias"] = (
            capo_connect.types.contact_flow_alias_info.deserialize_json(
                data["ContactFlowAlias"]
            )
        )
    return out
