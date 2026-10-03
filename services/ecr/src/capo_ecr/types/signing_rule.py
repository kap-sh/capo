"""Generated from Smithy shape ``com.amazonaws.ecr#SigningRule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecr.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecr.types.signing_profile_arn
    import capo_ecr.types.signing_repository_filter_list


class SigningRule(TypedDict, closed=True):
    signing_profile_arn: "capo_ecr.types.signing_profile_arn.SigningProfileArn"
    """<p>The ARN of the Amazon Web Services Signer signing profile to use for signing images that match this rule. For more information about signing profiles, see <a href="https://docs.aws.amazon.com/signer/latest/developerguide/signing-profiles.html">Signing profiles</a> in the <i>Amazon Web Services Signer Developer Guide</i>.</p>"""
    repository_filters: NotRequired[
        "capo_ecr.types.signing_repository_filter_list.SigningRepositoryFilterList"
    ]
    """<p>A list of repository filters that determine which repositories have their images signed on push. If no filters are specified, all images pushed to the registry are signed using the rule's signing profile. Maximum of 100 filters per rule.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningRule) -> dict:
    out: dict = {}
    out["signingProfileArn"] = value["signing_profile_arn"]
    if "repository_filters" in value:
        import capo_ecr.types.signing_repository_filter_list

        out["repositoryFilters"] = (
            capo_ecr.types.signing_repository_filter_list.serialize_aws_json_1_1(
                value["repository_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SigningRule:
    out: SigningRule = {}  # type: ignore[typeddict-item]
    if data.get("signingProfileArn") is not None:
        out["signing_profile_arn"] = data["signingProfileArn"]
    else:
        raise DeserializationError("SigningRule.signing_profile_arn required")
    if data.get("repositoryFilters") is not None:
        import capo_ecr.types.signing_repository_filter_list

        out["repository_filters"] = (
            capo_ecr.types.signing_repository_filter_list.deserialize_aws_json_1_1(
                data["repositoryFilters"]
            )
        )
    return out
