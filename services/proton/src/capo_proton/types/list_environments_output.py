"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.environment_summary_list
    import capo_proton.types.next_token


class ListEnvironmentsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next environment in the array of environments, after the current requested list of environments.</p>"""
    environments: "capo_proton.types.environment_summary_list.EnvironmentSummaryList"
    """<p>An array of environment detail data summaries.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.environment_summary_list

    out["environments"] = (
        capo_proton.types.environment_summary_list.serialize_aws_json_1_0(
            value["environments"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentsOutput:
    out: ListEnvironmentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("environments") is not None:
        import capo_proton.types.environment_summary_list

        out["environments"] = (
            capo_proton.types.environment_summary_list.deserialize_aws_json_1_0(
                data["environments"]
            )
        )
    else:
        out["environments"] = []
    return out


def redact_sensitive(value: ListEnvironmentsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "environments" in value:
        import capo_proton.types.environment_summary_list

        out["environments"] = (
            capo_proton.types.environment_summary_list.redact_sensitive(
                value["environments"]
            )
        )
    return out
