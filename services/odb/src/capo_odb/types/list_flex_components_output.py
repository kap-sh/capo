"""Generated from Smithy shape ``com.amazonaws.odb#ListFlexComponentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_odb.types.flex_component_list


class ListFlexComponentsOutput(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token to include in another request to get the next page of items. This value is <code>null</code> when there are no more items to return.</p>"""
    flex_components: "capo_odb.types.flex_component_list.FlexComponentList"
    """<p>The list of flex components along with their properties.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFlexComponentsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_odb.types.flex_component_list

    out["flexComponents"] = capo_odb.types.flex_component_list.serialize_aws_json_1_0(
        value["flex_components"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFlexComponentsOutput:
    out: ListFlexComponentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("flexComponents") is not None:
        import capo_odb.types.flex_component_list

        out["flex_components"] = (
            capo_odb.types.flex_component_list.deserialize_aws_json_1_0(
                data["flexComponents"]
            )
        )
    else:
        out["flex_components"] = []
    return out
