"""Generated from Smithy shape ``com.amazonaws.sts#AssumeRootResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.credentials
    import capo_sts.types.session_token_size_type
    import capo_sts.types.session_token_utilization_type
    import capo_sts.types.source_identity_type


class AssumeRootResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    source_identity: NotRequired[
        "capo_sts.types.source_identity_type.sourceIdentityType"
    ]
    """<p>The source identity specified by the principal that is calling the <code>AssumeRoot</code> operation.</p> <p>You can use the <code>aws:SourceIdentity</code> condition key to control access based on the value of source identity. For more information about using source identity, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_monitor.html">Monitor and control actions taken with assumed roles</a> in the <i>IAM User Guide</i>.</p> <p>The regex used to validate this parameter is a string of characters consisting of upper- and lower-case alphanumeric characters with no spaces. You can also include underscores or any of the following characters: =,.@-</p>"""
    session_token_utilization: NotRequired[
        "capo_sts.types.session_token_utilization_type.sessionTokenUtilizationType"
    ]
    session_token_size: NotRequired[
        "capo_sts.types.session_token_size_type.sessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: AssumeRootResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{key_prefix}Credentials"
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


def deserialize_query(el: Element) -> AssumeRootResponse:
    out: AssumeRootResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
        )
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
