"""Generated from Smithy shape ``com.amazonaws.proton#ListComponentsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.component_summary_list
    import capo_proton.types.next_token


class ListComponentsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next component in the array of components, after the current requested list of components.</p>"""
    components: "capo_proton.types.component_summary_list.ComponentSummaryList"
    """<p>An array of components with summary data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListComponentsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.component_summary_list

    out["components"] = capo_proton.types.component_summary_list.serialize_aws_json_1_0(
        value["components"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListComponentsOutput:
    out: ListComponentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("components") is not None:
        import capo_proton.types.component_summary_list

        out["components"] = (
            capo_proton.types.component_summary_list.deserialize_aws_json_1_0(
                data["components"]
            )
        )
    else:
        out["components"] = []
    return out


def redact_sensitive(value: ListComponentsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "components" in value:
        import capo_proton.types.component_summary_list

        out["components"] = capo_proton.types.component_summary_list.redact_sensitive(
            value["components"]
        )
    return out
