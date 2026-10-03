"""Generated from Smithy shape ``com.amazonaws.cloudformation#TypeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudformation._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudformation.types.description
    import capo_cloudformation.types.identity_provider
    import capo_cloudformation.types.is_activated
    import capo_cloudformation.types.public_version_number
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.publisher_name
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.timestamp
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.type_version_id


class TypeSummary(TypedDict, closed=True):
    type: NotRequired["capo_cloudformation.types.registry_type.RegistryType"]
    """<p>The kind of extension.</p>"""
    type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>The name of the extension.</p> <p>If you specified a <code>TypeNameAlias</code> when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a> API operation in your account and Region, CloudFormation considers that alias as the type name.</p>"""
    default_version_id: NotRequired[
        "capo_cloudformation.types.type_version_id.TypeVersionId"
    ]
    """<p>The ID of the default version of the extension. The default version is used when the extension version isn't specified.</p> <p>This applies only to private extensions you have registered in your account. For public extensions, both those provided by Amazon and published by third parties, CloudFormation returns <code>null</code>. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>To set the default version of an extension, use <a>SetTypeDefaultVersion</a>.</p>"""
    type_arn: NotRequired["capo_cloudformation.types.type_arn.TypeArn"]
    """<p>The ARN of the extension.</p>"""
    last_updated: NotRequired["capo_cloudformation.types.timestamp.Timestamp"]
    """<p>When the specified extension version was registered. This applies only to:</p> <ul> <li> <p>Private extensions you have registered in your account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> </li> <li> <p>Public extensions you have activated in your account with auto-update specified. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a>.</p> </li> </ul> <p>For all other extension types, CloudFormation returns <code>null</code>.</p>"""
    description: NotRequired["capo_cloudformation.types.description.Description"]
    """<p>The description of the extension.</p>"""
    publisher_id: NotRequired["capo_cloudformation.types.publisher_id.PublisherId"]
    """<p>The ID of the extension publisher, if the extension is published by a third party. Extensions published by Amazon don't return a publisher ID.</p>"""
    original_type_name: NotRequired["capo_cloudformation.types.type_name.TypeName"]
    """<p>For public extensions that have been activated for this account and Region, the type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and Region, CloudFormation treats that alias as the extension's type name within the account and Region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Use aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""
    public_version_number: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>For public extensions that have been activated for this account and Region, the version of the public extension to be used for CloudFormation operations in this account and Region.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and Region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""
    latest_public_version: NotRequired[
        "capo_cloudformation.types.public_version_number.PublicVersionNumber"
    ]
    """<p>For public extensions that have been activated for this account and Region, the latest version of the public extension <i>that is available</i>. For any extensions other than activated third-party extensions, CloudFormation returns <code>null</code>.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and Region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>"""
    publisher_identity: NotRequired[
        "capo_cloudformation.types.identity_provider.IdentityProvider"
    ]
    """<p>The service used to verify the publisher identity.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>"""
    publisher_name: NotRequired[
        "capo_cloudformation.types.publisher_name.PublisherName"
    ]
    """<p>The publisher name, as defined in the public profile for that publisher in the service used to verify the publisher identity.</p>"""
    is_activated: NotRequired["capo_cloudformation.types.is_activated.IsActivated"]
    """<p>Whether the extension is activated for this account and Region.</p> <p>This applies only to third-party public extensions. Extensions published by Amazon are activated by default.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TypeSummary, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        import capo_cloudformation.types.registry_type

        capo_cloudformation.types.registry_type.serialize_query(
            value["type"], pairs, f"{key_prefix}Type"
        )
    if "type_name" in value:
        pairs.append((f"{key_prefix}TypeName", str(value["type_name"])))
    if "default_version_id" in value:
        pairs.append(
            (f"{key_prefix}DefaultVersionId", str(value["default_version_id"]))
        )
    if "type_arn" in value:
        pairs.append((f"{key_prefix}TypeArn", str(value["type_arn"])))
    if "last_updated" in value:
        import capo_cloudformation.types.timestamp

        capo_cloudformation.types.timestamp.serialize_query(
            value["last_updated"], pairs, f"{key_prefix}LastUpdated"
        )
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "publisher_id" in value:
        pairs.append((f"{key_prefix}PublisherId", str(value["publisher_id"])))
    if "original_type_name" in value:
        pairs.append(
            (f"{key_prefix}OriginalTypeName", str(value["original_type_name"]))
        )
    if "public_version_number" in value:
        pairs.append(
            (f"{key_prefix}PublicVersionNumber", str(value["public_version_number"]))
        )
    if "latest_public_version" in value:
        pairs.append(
            (f"{key_prefix}LatestPublicVersion", str(value["latest_public_version"]))
        )
    if "publisher_identity" in value:
        import capo_cloudformation.types.identity_provider

        capo_cloudformation.types.identity_provider.serialize_query(
            value["publisher_identity"], pairs, f"{key_prefix}PublisherIdentity"
        )
    if "publisher_name" in value:
        pairs.append((f"{key_prefix}PublisherName", str(value["publisher_name"])))
    if "is_activated" in value:
        pairs.append(
            (f"{key_prefix}IsActivated", "true" if value["is_activated"] else "false")
        )


def deserialize_query(el: Element) -> TypeSummary:
    out: TypeSummary = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        import capo_cloudformation.types.registry_type

        out["type"] = capo_cloudformation.types.registry_type.deserialize_query(
            child_type
        )
    child_type_name = el.find("TypeName")
    if child_type_name is not None:
        out["type_name"] = str(child_type_name.text or "")
    child_default_version_id = el.find("DefaultVersionId")
    if child_default_version_id is not None:
        out["default_version_id"] = str(child_default_version_id.text or "")
    child_type_arn = el.find("TypeArn")
    if child_type_arn is not None:
        out["type_arn"] = str(child_type_arn.text or "")
    child_last_updated = el.find("LastUpdated")
    if child_last_updated is not None:
        import capo_cloudformation.types.timestamp

        out["last_updated"] = capo_cloudformation.types.timestamp.deserialize_query(
            child_last_updated
        )
    child_description = el.find("Description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_publisher_id = el.find("PublisherId")
    if child_publisher_id is not None:
        out["publisher_id"] = str(child_publisher_id.text or "")
    child_original_type_name = el.find("OriginalTypeName")
    if child_original_type_name is not None:
        out["original_type_name"] = str(child_original_type_name.text or "")
    child_public_version_number = el.find("PublicVersionNumber")
    if child_public_version_number is not None:
        out["public_version_number"] = str(child_public_version_number.text or "")
    child_latest_public_version = el.find("LatestPublicVersion")
    if child_latest_public_version is not None:
        out["latest_public_version"] = str(child_latest_public_version.text or "")
    child_publisher_identity = el.find("PublisherIdentity")
    if child_publisher_identity is not None:
        import capo_cloudformation.types.identity_provider

        out["publisher_identity"] = (
            capo_cloudformation.types.identity_provider.deserialize_query(
                child_publisher_identity
            )
        )
    child_publisher_name = el.find("PublisherName")
    if child_publisher_name is not None:
        out["publisher_name"] = str(child_publisher_name.text or "")
    child_is_activated = el.find("IsActivated")
    if child_is_activated is not None:
        out["is_activated"] = (child_is_activated.text or "").lower() == "true"
    return out
