"""Generated from Smithy shape ``com.amazonaws.controltower#ListEnabledBaselinesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_controltower.types.enabled_baselines
    import capo_controltower.types.list_enabled_baselines_next_token


class ListEnabledBaselinesOutput(TypedDict, closed=True):
    enabled_baselines: "capo_controltower.types.enabled_baselines.EnabledBaselines"
    """<p>Retuens a list of summaries of <code>EnabledBaseline</code> resources.</p>"""
    next_token: NotRequired[
        "capo_controltower.types.list_enabled_baselines_next_token.ListEnabledBaselinesNextToken"
    ]
    """<p>A pagination token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEnabledBaselinesOutput) -> dict:
    out: dict = {}
    import capo_controltower.types.enabled_baselines

    out["enabledBaselines"] = capo_controltower.types.enabled_baselines.serialize_json(
        value["enabled_baselines"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEnabledBaselinesOutput:
    out: ListEnabledBaselinesOutput = {}  # type: ignore[typeddict-item]
    if data.get("enabledBaselines") is not None:
        import capo_controltower.types.enabled_baselines

        out["enabled_baselines"] = (
            capo_controltower.types.enabled_baselines.deserialize_json(
                data["enabledBaselines"]
            )
        )
    else:
        out["enabled_baselines"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
