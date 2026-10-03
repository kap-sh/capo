"""Generated from Smithy shape ``com.amazonaws.organizations#CreateOrganizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_organizations.types.organization_feature_set


class CreateOrganizationRequest(TypedDict, closed=True):
    feature_set: NotRequired[
        "capo_organizations.types.organization_feature_set.OrganizationFeatureSet"
    ]
    """<p>Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.</p> <ul> <li> <p> <code>CONSOLIDATED_BILLING</code>: All member accounts have their bills consolidated to and paid by the management account. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only">Consolidated billing</a> in the <i>Organizations User Guide</i>.</p> <p> The consolidated billing feature subset isn't available for organizations in the Amazon Web Services GovCloud (US) Region.</p> </li> <li> <p> <code>ALL</code>: In addition to all the features supported by the consolidated billing feature set, the management account can also apply any policy type to any member account in the organization. For more information, see <a href="https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all">All features</a> in the <i>Organizations User Guide</i>.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOrganizationRequest) -> dict:
    out: dict = {}
    if "feature_set" in value:
        import capo_organizations.types.organization_feature_set

        out["FeatureSet"] = (
            capo_organizations.types.organization_feature_set.serialize_aws_json_1_1(
                value["feature_set"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOrganizationRequest:
    out: CreateOrganizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("FeatureSet") is not None:
        import capo_organizations.types.organization_feature_set

        out["feature_set"] = (
            capo_organizations.types.organization_feature_set.deserialize_aws_json_1_1(
                data["FeatureSet"]
            )
        )
    return out
