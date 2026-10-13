"""Generated from Smithy shape ``com.amazonaws.ec2#VerifiedAccessTrustProvider``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.device_options
    import capo_ec2.types.device_trust_provider_type
    import capo_ec2.types.native_application_oidc_options
    import capo_ec2.types.oidc_options
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.trust_provider_type
    import capo_ec2.types.user_trust_provider_type
    import capo_ec2.types.verified_access_sse_specification_response


class VerifiedAccessTrustProvider(TypedDict, closed=True):
    verified_access_trust_provider_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services Verified Access trust provider.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>A description for the Amazon Web Services Verified Access trust provider.</p>"""
    trust_provider_type: NotRequired[
        "capo_ec2.types.trust_provider_type.TrustProviderType"
    ]
    """<p>The type of Verified Access trust provider.</p>"""
    user_trust_provider_type: NotRequired[
        "capo_ec2.types.user_trust_provider_type.UserTrustProviderType"
    ]
    """<p>The type of user-based trust provider.</p>"""
    device_trust_provider_type: NotRequired[
        "capo_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
    ]
    """<p>The type of device-based trust provider.</p>"""
    oidc_options: NotRequired["capo_ec2.types.oidc_options.OidcOptions"]
    """<p>The options for an OpenID Connect-compatible user-identity trust provider.</p>"""
    device_options: NotRequired["capo_ec2.types.device_options.DeviceOptions"]
    """<p>The options for device-identity trust provider.</p>"""
    policy_reference_name: NotRequired["capo_ec2.types.string.String"]
    """<p>The identifier to be used when working with policy rules.</p>"""
    creation_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The creation time.</p>"""
    last_updated_time: NotRequired["capo_ec2.types.string.String"]
    """<p>The last updated time.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>The tags.</p>"""
    sse_specification: NotRequired[
        "capo_ec2.types.verified_access_sse_specification_response.VerifiedAccessSseSpecificationResponse"
    ]
    """<p>The options in use for server side encryption.</p>"""
    native_application_oidc_options: NotRequired[
        "capo_ec2.types.native_application_oidc_options.NativeApplicationOidcOptions"
    ]
    """<p>The OpenID Connect (OIDC) options.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VerifiedAccessTrustProvider, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "verified_access_trust_provider_id" in value:
        pairs.append(
            (
                f"{key_prefix}VerifiedAccessTrustProviderId",
                str(value["verified_access_trust_provider_id"]),
            )
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "trust_provider_type" in value:
        import capo_ec2.types.trust_provider_type

        capo_ec2.types.trust_provider_type.serialize_ec2_query(
            value["trust_provider_type"], pairs, f"{key_prefix}TrustProviderType"
        )
    if "user_trust_provider_type" in value:
        import capo_ec2.types.user_trust_provider_type

        capo_ec2.types.user_trust_provider_type.serialize_ec2_query(
            value["user_trust_provider_type"],
            pairs,
            f"{key_prefix}UserTrustProviderType",
        )
    if "device_trust_provider_type" in value:
        import capo_ec2.types.device_trust_provider_type

        capo_ec2.types.device_trust_provider_type.serialize_ec2_query(
            value["device_trust_provider_type"],
            pairs,
            f"{key_prefix}DeviceTrustProviderType",
        )
    if "oidc_options" in value:
        import capo_ec2.types.oidc_options

        capo_ec2.types.oidc_options.serialize_ec2_query(
            value["oidc_options"], pairs, f"{key_prefix}OidcOptions"
        )
    if "device_options" in value:
        import capo_ec2.types.device_options

        capo_ec2.types.device_options.serialize_ec2_query(
            value["device_options"], pairs, f"{key_prefix}DeviceOptions"
        )
    if "policy_reference_name" in value:
        pairs.append(
            (f"{key_prefix}PolicyReferenceName", str(value["policy_reference_name"]))
        )
    if "creation_time" in value:
        pairs.append((f"{key_prefix}CreationTime", str(value["creation_time"])))
    if "last_updated_time" in value:
        pairs.append((f"{key_prefix}LastUpdatedTime", str(value["last_updated_time"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "sse_specification" in value:
        import capo_ec2.types.verified_access_sse_specification_response

        capo_ec2.types.verified_access_sse_specification_response.serialize_ec2_query(
            value["sse_specification"], pairs, f"{key_prefix}SseSpecification"
        )
    if "native_application_oidc_options" in value:
        import capo_ec2.types.native_application_oidc_options

        capo_ec2.types.native_application_oidc_options.serialize_ec2_query(
            value["native_application_oidc_options"],
            pairs,
            f"{key_prefix}NativeApplicationOidcOptions",
        )


def deserialize_ec2_query(el: Element) -> VerifiedAccessTrustProvider:
    out: VerifiedAccessTrustProvider = {}  # type: ignore[typeddict-item]
    child_verified_access_trust_provider_id = el.find("verifiedAccessTrustProviderId")
    if child_verified_access_trust_provider_id is not None:
        out["verified_access_trust_provider_id"] = str(
            child_verified_access_trust_provider_id.text or ""
        )
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_trust_provider_type = el.find("trustProviderType")
    if child_trust_provider_type is not None:
        import capo_ec2.types.trust_provider_type

        out["trust_provider_type"] = (
            capo_ec2.types.trust_provider_type.deserialize_ec2_query(
                child_trust_provider_type
            )
        )
    child_user_trust_provider_type = el.find("userTrustProviderType")
    if child_user_trust_provider_type is not None:
        import capo_ec2.types.user_trust_provider_type

        out["user_trust_provider_type"] = (
            capo_ec2.types.user_trust_provider_type.deserialize_ec2_query(
                child_user_trust_provider_type
            )
        )
    child_device_trust_provider_type = el.find("deviceTrustProviderType")
    if child_device_trust_provider_type is not None:
        import capo_ec2.types.device_trust_provider_type

        out["device_trust_provider_type"] = (
            capo_ec2.types.device_trust_provider_type.deserialize_ec2_query(
                child_device_trust_provider_type
            )
        )
    child_oidc_options = el.find("oidcOptions")
    if child_oidc_options is not None:
        import capo_ec2.types.oidc_options

        out["oidc_options"] = capo_ec2.types.oidc_options.deserialize_ec2_query(
            child_oidc_options
        )
    child_device_options = el.find("deviceOptions")
    if child_device_options is not None:
        import capo_ec2.types.device_options

        out["device_options"] = capo_ec2.types.device_options.deserialize_ec2_query(
            child_device_options
        )
    child_policy_reference_name = el.find("policyReferenceName")
    if child_policy_reference_name is not None:
        out["policy_reference_name"] = str(child_policy_reference_name.text or "")
    child_creation_time = el.find("creationTime")
    if child_creation_time is not None:
        out["creation_time"] = str(child_creation_time.text or "")
    child_last_updated_time = el.find("lastUpdatedTime")
    if child_last_updated_time is not None:
        out["last_updated_time"] = str(child_last_updated_time.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_sse_specification = el.find("sseSpecification")
    if child_sse_specification is not None:
        import capo_ec2.types.verified_access_sse_specification_response

        out["sse_specification"] = (
            capo_ec2.types.verified_access_sse_specification_response.deserialize_ec2_query(
                child_sse_specification
            )
        )
    child_native_application_oidc_options = el.find("nativeApplicationOidcOptions")
    if child_native_application_oidc_options is not None:
        import capo_ec2.types.native_application_oidc_options

        out["native_application_oidc_options"] = (
            capo_ec2.types.native_application_oidc_options.deserialize_ec2_query(
                child_native_application_oidc_options
            )
        )
    return out


def redact_sensitive(value: VerifiedAccessTrustProvider) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "oidc_options" in value:
        import capo_ec2.types.oidc_options

        out["oidc_options"] = capo_ec2.types.oidc_options.redact_sensitive(
            value["oidc_options"]
        )
    return out
