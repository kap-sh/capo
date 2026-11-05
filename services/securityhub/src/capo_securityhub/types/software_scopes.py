"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareScopes``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.aws_organization_scope_list


class SoftwareScopes(TypedDict, closed=True):
    aws_organizations: NotRequired[
        "capo_securityhub.types.aws_organization_scope_list.AwsOrganizationScopeList"
    ]
    """<p>A list of Organizations scopes to include in the query results. Each entry in the list specifies an organization or organizational unit to include for the delegated administrator's account. If the list specifies multiple entries, the entries are combined using OR logic.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareScopes) -> dict:
    out: dict = {}
    if "aws_organizations" in value:
        import capo_securityhub.types.aws_organization_scope_list

        out["AwsOrganizations"] = (
            capo_securityhub.types.aws_organization_scope_list.serialize_json(
                value["aws_organizations"]
            )
        )
    return out


def deserialize_json(data: dict) -> SoftwareScopes:
    out: SoftwareScopes = {}  # type: ignore[typeddict-item]
    if data.get("AwsOrganizations") is not None:
        import capo_securityhub.types.aws_organization_scope_list

        out["aws_organizations"] = (
            capo_securityhub.types.aws_organization_scope_list.deserialize_json(
                data["AwsOrganizations"]
            )
        )
    return out
