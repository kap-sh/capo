"""Generated from Smithy shape ``com.amazonaws.cleanrooms#DifferentialPrivacyParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.differential_privacy_sensitivity_parameters_list


class DifferentialPrivacyParameters(TypedDict, closed=True):
    sensitivity_parameters: "capo_cleanrooms.types.differential_privacy_sensitivity_parameters_list.DifferentialPrivacySensitivityParametersList"
    """<p>Provides the sensitivity parameters that you can use to better understand the total amount of noise in query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DifferentialPrivacyParameters) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.differential_privacy_sensitivity_parameters_list

    out["sensitivityParameters"] = (
        capo_cleanrooms.types.differential_privacy_sensitivity_parameters_list.serialize_json(
            value["sensitivity_parameters"]
        )
    )
    return out


def deserialize_json(data: dict) -> DifferentialPrivacyParameters:
    out: DifferentialPrivacyParameters = {}  # type: ignore[typeddict-item]
    if data.get("sensitivityParameters") is not None:
        import capo_cleanrooms.types.differential_privacy_sensitivity_parameters_list

        out["sensitivity_parameters"] = (
            capo_cleanrooms.types.differential_privacy_sensitivity_parameters_list.deserialize_json(
                data["sensitivityParameters"]
            )
        )
    else:
        out["sensitivity_parameters"] = []
    return out
