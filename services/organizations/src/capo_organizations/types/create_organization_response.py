"""Generated from Smithy shape ``com.amazonaws.organizations#CreateOrganizationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.organization


class CreateOrganizationResponse(TypedDict, closed=True):
    organization: NotRequired["capo_organizations.types.organization.Organization"]
    """<p>A structure that contains details about the newly created organization.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOrganizationResponse) -> dict:
    out: dict = {}
    if "organization" in value:
        import capo_organizations.types.organization

        out["Organization"] = (
            capo_organizations.types.organization.serialize_aws_json_1_1(
                value["organization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOrganizationResponse:
    out: CreateOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Organization") is not None:
        import capo_organizations.types.organization

        out["organization"] = (
            capo_organizations.types.organization.deserialize_aws_json_1_1(
                data["Organization"]
            )
        )
    return out


def redact_sensitive(value: CreateOrganizationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "organization" in value:
        import capo_organizations.types.organization

        out["organization"] = capo_organizations.types.organization.redact_sensitive(
            value["organization"]
        )
    return out
