"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRoleWithWebIdentityResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.assumed_role_user
    import capo_sts.types.audience
    import capo_sts.types.credentials
    import capo_sts.types.issuer
    import capo_sts.types.non_negative_integer_type
    import capo_sts.types.session_token_size_type
    import capo_sts.types.session_token_utilization_type
    import capo_sts.types.source_identity_type
    import capo_sts.types.web_identity_subject_type


class AssumeRoleWithWebIdentityResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    subject_from_web_identity_token: NotRequired[
        "capo_sts.types.web_identity_subject_type.webIdentitySubjectType"
    ]
    """<p>The unique user identifier that is returned by the identity provider. This identifier is associated with the <code>WebIdentityToken</code> that was submitted with the <code>AssumeRoleWithWebIdentity</code> call. The identifier is typically unique to the user and the application that acquired the <code>WebIdentityToken</code> (pairwise identifier). For OpenID Connect ID tokens, this field contains the value returned by the identity provider as the token's <code>sub</code> (Subject) claim. </p>"""
    assumed_role_user: NotRequired["capo_sts.types.assumed_role_user.AssumedRoleUser"]
    """<p>The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting temporary security credentials. For example, you can reference these credentials as a principal in a resource-based policy by using the ARN or assumed role ID. The ARN and ID include the <code>RoleSessionName</code> that you specified when you called <code>AssumeRole</code>. </p>"""
    packed_policy_size: NotRequired[
        "capo_sts.types.non_negative_integer_type.nonNegativeIntegerType"
    ]
    """<p>A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.</p>"""
    provider: NotRequired["capo_sts.types.issuer.Issuer"]
    """<p> The issuing authority of the web identity token presented. For OpenID Connect ID tokens, this contains the value of the <code>iss</code> field. For OAuth 2.0 access tokens, this contains the value of the <code>ProviderId</code> parameter that was passed in the <code>AssumeRoleWithWebIdentity</code> request.</p>"""
    audience: NotRequired["capo_sts.types.audience.Audience"]
    """<p>The intended audience (also known as client ID) of the web identity token. This is traditionally the client identifier issued to the application that requested the web identity token.</p>"""
    source_identity: NotRequired[
        "capo_sts.types.source_identity_type.sourceIdentityType"
    ]
    """<p>The value of the source identity that is returned in the JSON web token (JWT) from the identity provider.</p> <p>You can require users to set a source identity value when they assume a role. You do this by using the <code>sts:SourceIdentity</code> condition key in a role trust policy. That way, actions that are taken with the role are associated with that user. After the source identity is set, the value cannot be changed. It is present in the request for all actions that are taken by the role and persists across <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts">chained role</a> sessions. You can configure your identity provider to use an attribute associated with your users, like user name or email, as the source identity when calling <code>AssumeRoleWithWebIdentity</code>. You do this by adding a claim to the JSON web token. To learn more about OIDC tokens and claims, see <a href="https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-tokens-with-identity-providers.html">Using Tokens with User Pools</a> in the <i>Amazon Cognito Developer Guide</i>. For more information about using source identity, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>"""
    session_token_utilization: NotRequired[
        "capo_sts.types.session_token_utilization_type.sessionTokenUtilizationType"
    ]
    session_token_size: NotRequired[
        "capo_sts.types.session_token_size_type.sessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRoleWithWebIdentityResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{key_prefix}Credentials"
        )
    if "subject_from_web_identity_token" in value:
        pairs.append(
            (
                f"{key_prefix}SubjectFromWebIdentityToken",
                str(value["subject_from_web_identity_token"]),
            )
        )
    if "assumed_role_user" in value:
        import capo_sts.types.assumed_role_user

        capo_sts.types.assumed_role_user.serialize_query(
            value["assumed_role_user"], pairs, f"{key_prefix}AssumedRoleUser"
        )
    if "packed_policy_size" in value:
        pairs.append(
            (f"{key_prefix}PackedPolicySize", str(value["packed_policy_size"]))
        )
    if "provider" in value:
        pairs.append((f"{key_prefix}Provider", str(value["provider"])))
    if "audience" in value:
        pairs.append((f"{key_prefix}Audience", str(value["audience"])))
    if "source_identity" in value:
        pairs.append((f"{key_prefix}SourceIdentity", str(value["source_identity"])))
    if "session_token_utilization" in value:
        pairs.append(
            (
                f"{key_prefix}SessionTokenUtilization",
                str(value["session_token_utilization"]),
            )
        )
    if "session_token_size" in value:
        pairs.append(
            (f"{key_prefix}SessionTokenSize", str(value["session_token_size"]))
        )


def deserialize_query(el: Element) -> AssumeRoleWithWebIdentityResponse:
    out: AssumeRoleWithWebIdentityResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
        )
    child_subject_from_web_identity_token = el.find("SubjectFromWebIdentityToken")
    if child_subject_from_web_identity_token is not None:
        out["subject_from_web_identity_token"] = str(
            child_subject_from_web_identity_token.text or ""
        )
    child_assumed_role_user = el.find("AssumedRoleUser")
    if child_assumed_role_user is not None:
        import capo_sts.types.assumed_role_user

        out["assumed_role_user"] = capo_sts.types.assumed_role_user.deserialize_query(
            child_assumed_role_user
        )
    child_packed_policy_size = el.find("PackedPolicySize")
    if child_packed_policy_size is not None:
        out["packed_policy_size"] = int(child_packed_policy_size.text or "")
    child_provider = el.find("Provider")
    if child_provider is not None:
        out["provider"] = str(child_provider.text or "")
    child_audience = el.find("Audience")
    if child_audience is not None:
        out["audience"] = str(child_audience.text or "")
    child_source_identity = el.find("SourceIdentity")
    if child_source_identity is not None:
        out["source_identity"] = str(child_source_identity.text or "")
    child_session_token_utilization = el.find("SessionTokenUtilization")
    if child_session_token_utilization is not None:
        out["session_token_utilization"] = int(
            child_session_token_utilization.text or ""
        )
    child_session_token_size = el.find("SessionTokenSize")
    if child_session_token_size is not None:
        out["session_token_size"] = int(child_session_token_size.text or "")
    return out
