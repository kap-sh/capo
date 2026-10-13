"""Generated from Smithy shape ``com.amazonaws.ssm#UpdateAssociationResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_description


class UpdateAssociationResult(TypedDict, closed=True):
    association_description: NotRequired[
        "capo_ssm.types.association_description.AssociationDescription"
    ]
    """<p>The description of the association that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateAssociationResult) -> dict:
    out: dict = {}
    if "association_description" in value:
        import capo_ssm.types.association_description

        out["AssociationDescription"] = (
            capo_ssm.types.association_description.serialize_aws_json_1_1(
                value["association_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateAssociationResult:
    out: UpdateAssociationResult = {}  # type: ignore[typeddict-item]
    if data.get("AssociationDescription") is not None:
        import capo_ssm.types.association_description

        out["association_description"] = (
            capo_ssm.types.association_description.deserialize_aws_json_1_1(
                data["AssociationDescription"]
            )
        )
    return out


def redact_sensitive(value: UpdateAssociationResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "association_description" in value:
        import capo_ssm.types.association_description

        out["association_description"] = (
            capo_ssm.types.association_description.redact_sensitive(
                value["association_description"]
            )
        )
    return out
