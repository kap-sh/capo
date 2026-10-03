"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVerifiedAccessTrustProviderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.modify_verified_access_native_application_oidc_options
    import capo_ec2.types.modify_verified_access_trust_provider_device_options
    import capo_ec2.types.modify_verified_access_trust_provider_oidc_options
    import capo_ec2.types.string
    import capo_ec2.types.verified_access_sse_specification_request
    import capo_ec2.types.verified_access_trust_provider_id


class ModifyVerifiedAccessTrustProviderRequest(TypedDict, closed=True):
    verified_access_trust_provider_id: NotRequired[
        "capo_ec2.types.verified_access_trust_provider_id.VerifiedAccessTrustProviderId"
    ]
    """<p>The ID of the Verified Access trust provider.</p>"""
    oidc_options: NotRequired[
        "capo_ec2.types.modify_verified_access_trust_provider_oidc_options.ModifyVerifiedAccessTrustProviderOidcOptions"
    ]
    """<p>The options for an OpenID Connect-compatible user-identity trust provider.</p>"""
    device_options: NotRequired[
        "capo_ec2.types.modify_verified_access_trust_provider_device_options.ModifyVerifiedAccessTrustProviderDeviceOptions"
    ]
    """<p>The options for a device-based trust provider. This parameter is required when the provider type is <code>device</code>.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Verified Access trust provider.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    sse_specification: NotRequired[
        "capo_ec2.types.verified_access_sse_specification_request.VerifiedAccessSseSpecificationRequest"
    ]
    """<p>The options for server side encryption.</p>"""
    native_application_oidc_options: NotRequired[
        "capo_ec2.types.modify_verified_access_native_application_oidc_options.ModifyVerifiedAccessNativeApplicationOidcOptions"
    ]
    """<p>The OpenID Connect (OIDC) options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVerifiedAccessTrustProviderRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_trust_provider_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessTrustProviderId",
                str(value["verified_access_trust_provider_id"]),
            )
        )
    if "oidc_options" in value:
        import capo_ec2.types.modify_verified_access_trust_provider_oidc_options

        capo_ec2.types.modify_verified_access_trust_provider_oidc_options.serialize_ec2_query(
            value["oidc_options"], pairs, f"{key_prefix}OidcOptions"
        )
    if "device_options" in value:
        import capo_ec2.types.modify_verified_access_trust_provider_device_options

        capo_ec2.types.modify_verified_access_trust_provider_device_options.serialize_ec2_query(
            value["device_options"], pairs, f"{key_prefix}DeviceOptions"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "sse_specification" in value:
        import capo_ec2.types.verified_access_sse_specification_request

        capo_ec2.types.verified_access_sse_specification_request.serialize_ec2_query(
            value["sse_specification"], pairs, f"{key_prefix}SseSpecification"
        )
    if "native_application_oidc_options" in value:
        import capo_ec2.types.modify_verified_access_native_application_oidc_options

        capo_ec2.types.modify_verified_access_native_application_oidc_options.serialize_ec2_query(
            value["native_application_oidc_options"],
            pairs,
            f"{key_prefix}NativeApplicationOidcOptions",
        )


def deserialize_ec2_query(el: Element) -> ModifyVerifiedAccessTrustProviderRequest:
    out: ModifyVerifiedAccessTrustProviderRequest = {}  # type: ignore[typeddict-item]
    child_verified_access_trust_provider_id = el.find("VerifiedAccessTrustProviderId")
    if child_verified_access_trust_provider_id is not None:
        out["verified_access_trust_provider_id"] = str(
            child_verified_access_trust_provider_id.text or ""
        )
    child_oidc_options = el.find("OidcOptions")
    if child_oidc_options is not None:
        import capo_ec2.types.modify_verified_access_trust_provider_oidc_options

        out["oidc_options"] = (
            capo_ec2.types.modify_verified_access_trust_provider_oidc_options.deserialize_ec2_query(
                child_oidc_options
            )
        )
    child_device_options = el.find("DeviceOptions")
    if child_device_options is not None:
        import capo_ec2.types.modify_verified_access_trust_provider_device_options

        out["device_options"] = (
            capo_ec2.types.modify_verified_access_trust_provider_device_options.deserialize_ec2_query(
                child_device_options
            )
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_sse_specification = el.find("SseSpecification")
    if child_sse_specification is not None:
        import capo_ec2.types.verified_access_sse_specification_request

        out["sse_specification"] = (
            capo_ec2.types.verified_access_sse_specification_request.deserialize_ec2_query(
                child_sse_specification
            )
        )
    child_native_application_oidc_options = el.find("NativeApplicationOidcOptions")
    if child_native_application_oidc_options is not None:
        import capo_ec2.types.modify_verified_access_native_application_oidc_options

        out["native_application_oidc_options"] = (
            capo_ec2.types.modify_verified_access_native_application_oidc_options.deserialize_ec2_query(
                child_native_application_oidc_options
            )
        )
    return out
