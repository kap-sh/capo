"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ReceiverConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.analysis_type
    import capo_cleanrooms.types.configuration_details


class ReceiverConfiguration(TypedDict, closed=True):
    analysis_type: "capo_cleanrooms.types.analysis_type.AnalysisType"
    """<p> The type of analysis for the protected query. The results of the query can be analyzed directly (<code>DIRECT_ANALYSIS</code>) or used as input into additional analyses (<code>ADDITIONAL_ANALYSIS</code>), such as a query that is a seed for a lookalike ML model.</p>"""
    configuration_details: NotRequired[
        "capo_cleanrooms.types.configuration_details.ConfigurationDetails"
    ]
    """<p> The configuration details of the receiver configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReceiverConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.analysis_type

    out["analysisType"] = capo_cleanrooms.types.analysis_type.serialize_json(
        value["analysis_type"]
    )
    if "configuration_details" in value:
        import capo_cleanrooms.types.configuration_details

        out["configurationDetails"] = (
            capo_cleanrooms.types.configuration_details.serialize_json(
                value["configuration_details"]
            )
        )
    return out


def deserialize_json(data: dict) -> ReceiverConfiguration:
    out: ReceiverConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("analysisType") is not None:
        import capo_cleanrooms.types.analysis_type

        out["analysis_type"] = capo_cleanrooms.types.analysis_type.deserialize_json(
            data["analysisType"]
        )
    else:
        import typing

        out["analysis_type"] = typing.cast(
            "capo_cleanrooms.types.analysis_type.AnalysisType", ""
        )
    if data.get("configurationDetails") is not None:
        import capo_cleanrooms.types.configuration_details

        out["configuration_details"] = (
            capo_cleanrooms.types.configuration_details.deserialize_json(
                data["configurationDetails"]
            )
        )
    return out
