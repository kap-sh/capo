"""Generated from Smithy shape ``com.amazonaws.verifiedpermissions#IdentitySourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_verifiedpermissions.types.client_ids
    import capo_verifiedpermissions.types.discovery_url
    import capo_verifiedpermissions.types.open_id_issuer
    import capo_verifiedpermissions.types.user_pool_arn


class IdentitySourceDetails(TypedDict, closed=True):
    client_ids: NotRequired["capo_verifiedpermissions.types.client_ids.ClientIds"]
    """<p>The application client IDs associated with the specified Amazon Cognito user pool that are enabled for this identity source.</p>"""
    user_pool_arn: NotRequired[
        "capo_verifiedpermissions.types.user_pool_arn.UserPoolArn"
    ]
    """<p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">Amazon Resource Name (ARN)</a> of the Amazon Cognito user pool whose identities are accessible to this Verified Permissions policy store.</p>"""
    discovery_url: NotRequired[
        "capo_verifiedpermissions.types.discovery_url.DiscoveryUrl"
    ]
    """<p>The well-known URL that points to this user pool's OIDC discovery endpoint. This is a URL string in the following format. This URL replaces the placeholders for both the Amazon Web Services Region and the user pool identifier with those appropriate for this user pool.</p> <p> <code>https://cognito-idp.<i>&lt;region&gt;</i>.amazonaws.com/<i>&lt;user-pool-id&gt;</i>/.well-known/openid-configuration</code> </p>"""
    open_id_issuer: NotRequired[
        "capo_verifiedpermissions.types.open_id_issuer.OpenIdIssuer"
    ]
    """<p>A string that identifies the type of OIDC service represented by this identity source. </p> <p>At this time, the only valid value is <code>cognito</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: IdentitySourceDetails) -> dict:
    out: dict = {}
    if "client_ids" in value:
        import capo_verifiedpermissions.types.client_ids

        out["clientIds"] = (
            capo_verifiedpermissions.types.client_ids.serialize_aws_json_1_0(
                value["client_ids"]
            )
        )
    if "user_pool_arn" in value:
        out["userPoolArn"] = value["user_pool_arn"]
    if "discovery_url" in value:
        out["discoveryUrl"] = value["discovery_url"]
    if "open_id_issuer" in value:
        import capo_verifiedpermissions.types.open_id_issuer

        out["openIdIssuer"] = (
            capo_verifiedpermissions.types.open_id_issuer.serialize_aws_json_1_0(
                value["open_id_issuer"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> IdentitySourceDetails:
    out: IdentitySourceDetails = {}  # type: ignore[typeddict-item]
    if data.get("clientIds") is not None:
        import capo_verifiedpermissions.types.client_ids

        out["client_ids"] = (
            capo_verifiedpermissions.types.client_ids.deserialize_aws_json_1_0(
                data["clientIds"]
            )
        )
    if data.get("userPoolArn") is not None:
        out["user_pool_arn"] = data["userPoolArn"]
    if data.get("discoveryUrl") is not None:
        out["discovery_url"] = data["discoveryUrl"]
    if data.get("openIdIssuer") is not None:
        import capo_verifiedpermissions.types.open_id_issuer

        out["open_id_issuer"] = (
            capo_verifiedpermissions.types.open_id_issuer.deserialize_aws_json_1_0(
                data["openIdIssuer"]
            )
        )
    return out
