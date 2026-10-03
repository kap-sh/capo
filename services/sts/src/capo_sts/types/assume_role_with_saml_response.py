"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRoleWithSAMLResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.assumed_role_user
    import capo_sts.types.audience
    import capo_sts.types.credentials
    import capo_sts.types.issuer
    import capo_sts.types.name_qualifier
    import capo_sts.types.non_negative_integer_type
    import capo_sts.types.session_token_size_type
    import capo_sts.types.session_token_utilization_type
    import capo_sts.types.source_identity_type
    import capo_sts.types.subject
    import capo_sts.types.subject_type


class AssumeRoleWithSAMLResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    assumed_role_user: NotRequired["capo_sts.types.assumed_role_user.AssumedRoleUser"]
    """<p>The identifiers for the temporary security credentials that the operation returns.</p>"""
    packed_policy_size: NotRequired[
        "capo_sts.types.non_negative_integer_type.nonNegativeIntegerType"
    ]
    """<p>A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.</p>"""
    subject: NotRequired["capo_sts.types.subject.Subject"]
    """<p>The value of the <code>NameID</code> element in the <code>Subject</code> element of the SAML assertion.</p>"""
    subject_type: NotRequired["capo_sts.types.subject_type.SubjectType"]
    """<p> The format of the name ID, as defined by the <code>Format</code> attribute in the <code>NameID</code> element of the SAML assertion. Typical examples of the format are <code>transient</code> or <code>persistent</code>. </p> <p> If the format includes the prefix <code>urn:oasis:names:tc:SAML:2.0:nameid-format</code>, that prefix is removed. For example, <code>urn:oasis:names:tc:SAML:2.0:nameid-format:transient</code> is returned as <code>transient</code>. If the format includes any other prefix, the format is returned with no modifications.</p>"""
    issuer: NotRequired["capo_sts.types.issuer.Issuer"]
    """<p>The value of the <code>Issuer</code> element of the SAML assertion.</p>"""
    audience: NotRequired["capo_sts.types.audience.Audience"]
    """<p> The value of the <code>Recipient</code> attribute of the <code>SubjectConfirmationData</code> element of the SAML assertion. </p>"""
    name_qualifier: NotRequired["capo_sts.types.name_qualifier.NameQualifier"]
    """<p>A hash value based on the concatenation of the following:</p> <ul> <li> <p>The <code>Issuer</code> response value.</p> </li> <li> <p>The Amazon Web Services account ID.</p> </li> <li> <p>The friendly name (the last part of the ARN) of the SAML provider in IAM.</p> </li> </ul> <p>The combination of <code>NameQualifier</code> and <code>Subject</code> can be used to uniquely identify a user.</p> <p>The following pseudocode shows how the hash value is calculated:</p> <p> <code>BASE64 ( SHA1 ( "https://example.com/saml" + "123456789012" + "/MySAMLIdP" ) )</code> </p>"""
    source_identity: NotRequired[
        "capo_sts.types.source_identity_type.sourceIdentityType"
    ]
    """<p>The value in the <code>SourceIdentity</code> attribute in the SAML assertion. The source identity value persists across <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#iam-term-role-chaining">chained role</a> sessions.</p> <p>You can require users to set a source identity value when they assume a role. You do this by using the <code>sts:SourceIdentity</code> condition key in a role trust policy. That way, actions that are taken with the role are associated with that user. After the source identity is set, the value cannot be changed. It is present in the request for all actions that are taken by the role and persists across <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts">chained role</a> sessions. You can configure your SAML identity provider to use an attribute associated with your users, like user name or email, as the source identity when calling <code>AssumeRoleWithSAML</code>. You do this by adding an attribute to the SAML assertion. For more information about using source identity, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>"""
    session_token_utilization: NotRequired[
        "capo_sts.types.session_token_utilization_type.sessionTokenUtilizationType"
    ]
    session_token_size: NotRequired[
        "capo_sts.types.session_token_size_type.sessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRoleWithSAMLResponse, pairs: list[tuple[str, str]], prefix: str
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
    if "subject" in value:
        pairs.append((f"{key_prefix}Subject", str(value["subject"])))
    if "subject_type" in value:
        pairs.append((f"{key_prefix}SubjectType", str(value["subject_type"])))
    if "issuer" in value:
        pairs.append((f"{key_prefix}Issuer", str(value["issuer"])))
    if "audience" in value:
        pairs.append((f"{key_prefix}Audience", str(value["audience"])))
    if "name_qualifier" in value:
        pairs.append((f"{key_prefix}NameQualifier", str(value["name_qualifier"])))
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


def deserialize_query(el: Element) -> AssumeRoleWithSAMLResponse:
    out: AssumeRoleWithSAMLResponse = {}  # type: ignore[typeddict-item]
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
    child_subject = el.find("Subject")
    if child_subject is not None:
        out["subject"] = str(child_subject.text or "")
    child_subject_type = el.find("SubjectType")
    if child_subject_type is not None:
        out["subject_type"] = str(child_subject_type.text or "")
    child_issuer = el.find("Issuer")
    if child_issuer is not None:
        out["issuer"] = str(child_issuer.text or "")
    child_audience = el.find("Audience")
    if child_audience is not None:
        out["audience"] = str(child_audience.text or "")
    child_name_qualifier = el.find("NameQualifier")
    if child_name_qualifier is not None:
        out["name_qualifier"] = str(child_name_qualifier.text or "")
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
