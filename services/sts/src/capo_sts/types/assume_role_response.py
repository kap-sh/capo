"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRoleResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.assumed_role_user
    import capo_sts.types.credentials
    import capo_sts.types.non_negative_integer_type
    import capo_sts.types.session_token_size_type
    import capo_sts.types.session_token_utilization_type
    import capo_sts.types.source_identity_type


class AssumeRoleResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    assumed_role_user: NotRequired["capo_sts.types.assumed_role_user.AssumedRoleUser"]
    """<p>The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you can use to refer to the resulting temporary security credentials. For example, you can reference these credentials as a principal in a resource-based policy by using the ARN or assumed role ID. The ARN and ID include the <code>RoleSessionName</code> that you specified when you called <code>AssumeRole</code>. </p>"""
    packed_policy_size: NotRequired[
        "capo_sts.types.non_negative_integer_type.nonNegativeIntegerType"
    ]
    """<p>A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.</p>"""
    source_identity: NotRequired[
        "capo_sts.types.source_identity_type.sourceIdentityType"
    ]
    """<p>The source identity specified by the principal that is calling the <code>AssumeRole</code> operation.</p> <p>You can require users to specify a source identity when they assume a role. You do this by using the <code>sts:SourceIdentity</code> condition key in a role trust policy. You can use source identity information in CloudTrail logs to determine who took actions with a role. You can use the <code>aws:SourceIdentity</code> condition key to further control access to Amazon Web Services resources based on the value of source identity. For more information about using source identity, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>"""
    session_token_utilization: NotRequired[
        "capo_sts.types.session_token_utilization_type.sessionTokenUtilizationType"
    ]
    session_token_size: NotRequired[
        "capo_sts.types.session_token_size_type.sessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRoleResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{key_prefix}Credentials"
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


def deserialize_query(el: Element) -> AssumeRoleResponse:
    out: AssumeRoleResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
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
