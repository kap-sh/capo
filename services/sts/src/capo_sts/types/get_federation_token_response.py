"""Generated from Smithy shape ``com.amazonaws.sts#GetFederationTokenResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_sts._protocol.xml import Element

if TYPE_CHECKING:
    import capo_sts.types.credentials
    import capo_sts.types.federated_user
    import capo_sts.types.non_negative_integer_type
    import capo_sts.types.session_token_size_type
    import capo_sts.types.session_token_utilization_type


class GetFederationTokenResponse(TypedDict, closed=True):
    credentials: NotRequired["capo_sts.types.credentials.Credentials"]
    """<p>The temporary security credentials, which include an access key ID, a secret access key, and a security (or session) token.</p> <note> <p>The size of the security token that STS API operations return is not fixed. We strongly recommend that you make no assumptions about the maximum size.</p> </note>"""
    federated_user: NotRequired["capo_sts.types.federated_user.FederatedUser"]
    """<p>Identifiers for the federated user associated with the credentials (such as <code>arn:aws:sts::123456789012:federated-user/Bob</code> or <code>123456789012:Bob</code>). You can use the federated user's ARN in your resource-based policies, such as an Amazon S3 bucket policy. </p>"""
    packed_policy_size: NotRequired[
        "capo_sts.types.non_negative_integer_type.nonNegativeIntegerType"
    ]
    """<p>A percentage value that indicates the packed size of the session policies and session tags combined passed in the request. The request fails if the packed size is greater than 100 percent, which means the policies and tags exceeded the allowed space.</p>"""
    session_token_utilization: NotRequired[
        "capo_sts.types.session_token_utilization_type.sessionTokenUtilizationType"
    ]
    session_token_size: NotRequired[
        "capo_sts.types.session_token_size_type.sessionTokenSizeType"
    ]


# --- awsQuery ser/de ---
def serialize_query(
    value: GetFederationTokenResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "credentials" in value:
        import capo_sts.types.credentials

        capo_sts.types.credentials.serialize_query(
            value["credentials"], pairs, f"{key_prefix}Credentials"
        )
    if "federated_user" in value:
        import capo_sts.types.federated_user

        capo_sts.types.federated_user.serialize_query(
            value["federated_user"], pairs, f"{key_prefix}FederatedUser"
        )
    if "packed_policy_size" in value:
        pairs.append(
            (f"{key_prefix}PackedPolicySize", str(value["packed_policy_size"]))
        )
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


def deserialize_query(el: Element) -> GetFederationTokenResponse:
    out: GetFederationTokenResponse = {}  # type: ignore[typeddict-item]
    child_credentials = el.find("Credentials")
    if child_credentials is not None:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.deserialize_query(
            child_credentials
        )
    child_federated_user = el.find("FederatedUser")
    if child_federated_user is not None:
        import capo_sts.types.federated_user

        out["federated_user"] = capo_sts.types.federated_user.deserialize_query(
            child_federated_user
        )
    child_packed_policy_size = el.find("PackedPolicySize")
    if child_packed_policy_size is not None:
        out["packed_policy_size"] = int(child_packed_policy_size.text or "")
    child_session_token_utilization = el.find("SessionTokenUtilization")
    if child_session_token_utilization is not None:
        out["session_token_utilization"] = int(
            child_session_token_utilization.text or ""
        )
    child_session_token_size = el.find("SessionTokenSize")
    if child_session_token_size is not None:
        out["session_token_size"] = int(child_session_token_size.text or "")
    return out


def redact_sensitive(value: GetFederationTokenResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "credentials" in value:
        import capo_sts.types.credentials

        out["credentials"] = capo_sts.types.credentials.redact_sensitive(
            value["credentials"]
        )
    return out
