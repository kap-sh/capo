"""Generated from Smithy shape ``com.amazonaws.organizations#DescribeOrganizationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.organization


class DescribeOrganizationResponse(TypedDict, closed=True):
    organization: NotRequired["capo_organizations.types.organization.Organization"]
    """<p>A structure that contains information about the organization.</p> <important> <p>The <code>AvailablePolicyTypes</code> part of the response is deprecated, and you shouldn't use it in your apps. It doesn't include any policy type supported by Organizations other than SCPs. In the China (Ningxia) Region, no policy type is included. To determine which policy types are enabled in your organization, use the <code> <a>ListRoots</a> </code> operation.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOrganizationResponse) -> dict:
    out: dict = {}
    if "organization" in value:
        import capo_organizations.types.organization

        out["Organization"] = (
            capo_organizations.types.organization.serialize_aws_json_1_1(
                value["organization"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOrganizationResponse:
    out: DescribeOrganizationResponse = {}  # type: ignore[typeddict-item]
    if data.get("Organization") is not None:
        import capo_organizations.types.organization

        out["organization"] = (
            capo_organizations.types.organization.deserialize_aws_json_1_1(
                data["Organization"]
            )
        )
    return out


def redact_sensitive(value: DescribeOrganizationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "organization" in value:
        import capo_organizations.types.organization

        out["organization"] = capo_organizations.types.organization.redact_sensitive(
            value["organization"]
        )
    return out
