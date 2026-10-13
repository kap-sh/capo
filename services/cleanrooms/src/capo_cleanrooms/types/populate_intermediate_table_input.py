"""Generated from Smithy shape ``com.amazonaws.cleanrooms#PopulateIntermediateTableInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.account_id
    import capo_cleanrooms.types.intermediate_table_compute_configuration
    import capo_cleanrooms.types.intermediate_table_identifier
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.parameter_map


class PopulateIntermediateTableInput(TypedDict, closed=True):
    intermediate_table_identifier: "capo_cleanrooms.types.intermediate_table_identifier.IntermediateTableIdentifier"
    """<p>The unique identifier of the intermediate table to populate.</p>"""
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership that contains the intermediate table.</p>"""
    parameters: NotRequired["capo_cleanrooms.types.parameter_map.ParameterMap"]
    """<p>The runtime parameter values that override the defaults in the stored query.</p>"""
    compute_configuration: NotRequired[
        "capo_cleanrooms.types.intermediate_table_compute_configuration.IntermediateTableComputeConfiguration"
    ]
    """<p>The compute configuration for the population query execution.</p>"""
    analysis_payer_account_id: NotRequired["capo_cleanrooms.types.account_id.AccountId"]
    """<p>The account ID of the member that pays for the analysis compute costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PopulateIntermediateTableInput) -> dict:
    out: dict = {}
    if "parameters" in value:
        import capo_cleanrooms.types.parameter_map

        out["parameters"] = capo_cleanrooms.types.parameter_map.serialize_json(
            value["parameters"]
        )
    if "compute_configuration" in value:
        import capo_cleanrooms.types.intermediate_table_compute_configuration

        out["computeConfiguration"] = (
            capo_cleanrooms.types.intermediate_table_compute_configuration.serialize_json(
                value["compute_configuration"]
            )
        )
    if "analysis_payer_account_id" in value:
        out["analysisPayerAccountId"] = value["analysis_payer_account_id"]
    return out


def deserialize_json(data: dict) -> PopulateIntermediateTableInput:
    out: PopulateIntermediateTableInput = {}  # type: ignore[typeddict-item]
    if data.get("parameters") is not None:
        import capo_cleanrooms.types.parameter_map

        out["parameters"] = capo_cleanrooms.types.parameter_map.deserialize_json(
            data["parameters"]
        )
    if data.get("computeConfiguration") is not None:
        import capo_cleanrooms.types.intermediate_table_compute_configuration

        out["compute_configuration"] = (
            capo_cleanrooms.types.intermediate_table_compute_configuration.deserialize_json(
                data["computeConfiguration"]
            )
        )
    if data.get("analysisPayerAccountId") is not None:
        out["analysis_payer_account_id"] = data["analysisPayerAccountId"]
    return out


def redact_sensitive(value: PopulateIntermediateTableInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "parameters" in value:
        out["parameters"] = "*** Sensitive Data Redacted ***"
    return out
