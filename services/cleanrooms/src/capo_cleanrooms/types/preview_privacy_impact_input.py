"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PreviewPrivacyImpactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.preview_privacy_impact_parameters_input


class PreviewPrivacyImpactInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>A unique identifier for one of your memberships for a collaboration. Accepts a membership ID.</p>"""
    parameters: "capo_cleanrooms.types.preview_privacy_impact_parameters_input.PreviewPrivacyImpactParametersInput"
    """<p>Specifies the desired epsilon and noise parameters to preview.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PreviewPrivacyImpactInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.preview_privacy_impact_parameters_input

    out["parameters"] = (
        capo_cleanrooms.types.preview_privacy_impact_parameters_input.serialize_json(
            value["parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> PreviewPrivacyImpactInput:
    out: PreviewPrivacyImpactInput = {}  # type: ignore[typeddict-item]
    if data.get("parameters") is not None:
        import capo_cleanrooms.types.preview_privacy_impact_parameters_input

        out["parameters"] = (
            capo_cleanrooms.types.preview_privacy_impact_parameters_input.deserialize_json(
                data["parameters"]
            )
        )
    else:
        out["parameters"] = {"$unknown": {"name": ""}}
    return out
