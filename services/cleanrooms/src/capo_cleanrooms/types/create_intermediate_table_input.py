"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateIntermediateTableInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_cleanrooms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanrooms.types.display_name
    import capo_cleanrooms.types.kms_key_arn
    import capo_cleanrooms.types.membership_identifier
    import capo_cleanrooms.types.population_analysis_configuration
    import capo_cleanrooms.types.resource_description
    import capo_cleanrooms.types.tag_map


class CreateIntermediateTableInput(TypedDict, closed=True):
    membership_identifier: (
        "capo_cleanrooms.types.membership_identifier.MembershipIdentifier"
    )
    """<p>The unique identifier of the membership where the intermediate table is created.</p>"""
    name: "capo_cleanrooms.types.display_name.DisplayName"
    """<p>The display name for the intermediate table.</p>"""
    description: NotRequired[
        "capo_cleanrooms.types.resource_description.ResourceDescription"
    ]
    """<p>A description of the intermediate table.</p>"""
    population_analysis_configuration: "capo_cleanrooms.types.population_analysis_configuration.PopulationAnalysisConfiguration"
    """<p>The configuration that defines the analysis used to populate the intermediate table.</p>"""
    kms_key_arn: NotRequired["capo_cleanrooms.types.kms_key_arn.KMSKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the customer-managed KMS key used to encrypt the intermediate table data.</p>"""
    retention_in_days: NotRequired["int"]
    """<p>The number of days to retain populated data versions.</p>"""
    tags: NotRequired["capo_cleanrooms.types.tag_map.TagMap"]
    """<p>An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIntermediateTableInput) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_cleanrooms.types.population_analysis_configuration

    out["populationAnalysisConfiguration"] = (
        capo_cleanrooms.types.population_analysis_configuration.serialize_json(
            value["population_analysis_configuration"]
        )
    )
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "retention_in_days" in value:
        out["retentionInDays"] = value["retention_in_days"]
    if "tags" in value:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIntermediateTableInput:
    out: CreateIntermediateTableInput = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateIntermediateTableInput.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("populationAnalysisConfiguration") is not None:
        import capo_cleanrooms.types.population_analysis_configuration

        out["population_analysis_configuration"] = (
            capo_cleanrooms.types.population_analysis_configuration.deserialize_json(
                data["populationAnalysisConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateIntermediateTableInput.population_analysis_configuration required"
        )
    if data.get("kmsKeyArn") is not None:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if data.get("retentionInDays") is not None:
        out["retention_in_days"] = data["retentionInDays"]
    if data.get("tags") is not None:
        import capo_cleanrooms.types.tag_map

        out["tags"] = capo_cleanrooms.types.tag_map.deserialize_json(data["tags"])
    return out


def redact_sensitive(value: CreateIntermediateTableInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "population_analysis_configuration" in value:
        import capo_cleanrooms.types.population_analysis_configuration

        out["population_analysis_configuration"] = (
            capo_cleanrooms.types.population_analysis_configuration.redact_sensitive(
                value["population_analysis_configuration"]
            )
        )
    return out
