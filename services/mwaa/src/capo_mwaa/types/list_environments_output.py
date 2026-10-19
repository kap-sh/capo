"""Generated from Smithy shape ``com.amazonaws.mwaa#ListEnvironmentsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa.types.environment_list
    import capo_mwaa.types.next_token


class ListEnvironmentsOutput(TypedDict, closed=True):
    environments: "capo_mwaa.types.environment_list.EnvironmentList"
    """<p>Returns a list of Amazon MWAA environments.</p>"""
    next_token: NotRequired["capo_mwaa.types.next_token.NextToken"]
    """<p>Retrieves the next page of the results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnvironmentsOutput) -> dict:
    out: dict = {}
    import capo_mwaa.types.environment_list

    out["Environments"] = capo_mwaa.types.environment_list.serialize_json(
        value["environments"]
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnvironmentsOutput:
    out: ListEnvironmentsOutput = {}  # type: ignore[typeddict-item]
    if data.get("Environments") is not None:
        import capo_mwaa.types.environment_list

        out["environments"] = capo_mwaa.types.environment_list.deserialize_json(
            data["Environments"]
        )
    else:
        out["environments"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
