"""Generated from Smithy shape ``com.amazonaws.codepipeline#ActionTypeDeclaration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codepipeline.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codepipeline.types.action_type_artifact_details
    import capo_codepipeline.types.action_type_description
    import capo_codepipeline.types.action_type_executor
    import capo_codepipeline.types.action_type_identifier
    import capo_codepipeline.types.action_type_permissions
    import capo_codepipeline.types.action_type_properties
    import capo_codepipeline.types.action_type_urls


class ActionTypeDeclaration(TypedDict, closed=True):
    description: NotRequired[
        "capo_codepipeline.types.action_type_description.ActionTypeDescription"
    ]
    """<p>The description for the action type to be updated.</p>"""
    executor: "capo_codepipeline.types.action_type_executor.ActionTypeExecutor"
    """<p>Information about the executor for an action type that was created with any supported integration model.</p>"""
    id: "capo_codepipeline.types.action_type_identifier.ActionTypeIdentifier"
    """<p>The action category, owner, provider, and version of the action type to be updated.</p>"""
    input_artifact_details: (
        "capo_codepipeline.types.action_type_artifact_details.ActionTypeArtifactDetails"
    )
    """<p>Details for the artifacts, such as application files, to be worked on by the action. For example, the minimum and maximum number of input artifacts allowed.</p>"""
    output_artifact_details: (
        "capo_codepipeline.types.action_type_artifact_details.ActionTypeArtifactDetails"
    )
    """<p>Details for the output artifacts, such as a built application, that are the result of the action. For example, the minimum and maximum number of output artifacts allowed.</p>"""
    permissions: NotRequired[
        "capo_codepipeline.types.action_type_permissions.ActionTypePermissions"
    ]
    """<p>Details identifying the accounts with permissions to use the action type.</p>"""
    properties: NotRequired[
        "capo_codepipeline.types.action_type_properties.ActionTypeProperties"
    ]
    """<p>The properties of the action type to be updated.</p>"""
    urls: NotRequired["capo_codepipeline.types.action_type_urls.ActionTypeUrls"]
    """<p>The links associated with the action type to be updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ActionTypeDeclaration) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_codepipeline.types.action_type_executor

    out["executor"] = (
        capo_codepipeline.types.action_type_executor.serialize_aws_json_1_1(
            value["executor"]
        )
    )
    import capo_codepipeline.types.action_type_identifier

    out["id"] = capo_codepipeline.types.action_type_identifier.serialize_aws_json_1_1(
        value["id"]
    )
    import capo_codepipeline.types.action_type_artifact_details

    out["inputArtifactDetails"] = (
        capo_codepipeline.types.action_type_artifact_details.serialize_aws_json_1_1(
            value["input_artifact_details"]
        )
    )
    import capo_codepipeline.types.action_type_artifact_details

    out["outputArtifactDetails"] = (
        capo_codepipeline.types.action_type_artifact_details.serialize_aws_json_1_1(
            value["output_artifact_details"]
        )
    )
    if "permissions" in value:
        import capo_codepipeline.types.action_type_permissions

        out["permissions"] = (
            capo_codepipeline.types.action_type_permissions.serialize_aws_json_1_1(
                value["permissions"]
            )
        )
    if "properties" in value:
        import capo_codepipeline.types.action_type_properties

        out["properties"] = (
            capo_codepipeline.types.action_type_properties.serialize_aws_json_1_1(
                value["properties"]
            )
        )
    if "urls" in value:
        import capo_codepipeline.types.action_type_urls

        out["urls"] = capo_codepipeline.types.action_type_urls.serialize_aws_json_1_1(
            value["urls"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ActionTypeDeclaration:
    out: ActionTypeDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executor") is not None:
        import capo_codepipeline.types.action_type_executor

        out["executor"] = (
            capo_codepipeline.types.action_type_executor.deserialize_aws_json_1_1(
                data["executor"]
            )
        )
    else:
        raise DeserializationError("ActionTypeDeclaration.executor required")
    if data.get("id") is not None:
        import capo_codepipeline.types.action_type_identifier

        out["id"] = (
            capo_codepipeline.types.action_type_identifier.deserialize_aws_json_1_1(
                data["id"]
            )
        )
    else:
        raise DeserializationError("ActionTypeDeclaration.id required")
    if data.get("inputArtifactDetails") is not None:
        import capo_codepipeline.types.action_type_artifact_details

        out["input_artifact_details"] = (
            capo_codepipeline.types.action_type_artifact_details.deserialize_aws_json_1_1(
                data["inputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "ActionTypeDeclaration.input_artifact_details required"
        )
    if data.get("outputArtifactDetails") is not None:
        import capo_codepipeline.types.action_type_artifact_details

        out["output_artifact_details"] = (
            capo_codepipeline.types.action_type_artifact_details.deserialize_aws_json_1_1(
                data["outputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "ActionTypeDeclaration.output_artifact_details required"
        )
    if data.get("permissions") is not None:
        import capo_codepipeline.types.action_type_permissions

        out["permissions"] = (
            capo_codepipeline.types.action_type_permissions.deserialize_aws_json_1_1(
                data["permissions"]
            )
        )
    if data.get("properties") is not None:
        import capo_codepipeline.types.action_type_properties

        out["properties"] = (
            capo_codepipeline.types.action_type_properties.deserialize_aws_json_1_1(
                data["properties"]
            )
        )
    if data.get("urls") is not None:
        import capo_codepipeline.types.action_type_urls

        out["urls"] = capo_codepipeline.types.action_type_urls.deserialize_aws_json_1_1(
            data["urls"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ActionTypeDeclaration) -> dict:
    out: dict = {}
    if "description" in value:
        out["description"] = value["description"]
    import capo_codepipeline.types.action_type_executor

    out["executor"] = capo_codepipeline.types.action_type_executor.serialize_cbor(
        value["executor"]
    )
    import capo_codepipeline.types.action_type_identifier

    out["id"] = capo_codepipeline.types.action_type_identifier.serialize_cbor(
        value["id"]
    )
    import capo_codepipeline.types.action_type_artifact_details

    out["inputArtifactDetails"] = (
        capo_codepipeline.types.action_type_artifact_details.serialize_cbor(
            value["input_artifact_details"]
        )
    )
    import capo_codepipeline.types.action_type_artifact_details

    out["outputArtifactDetails"] = (
        capo_codepipeline.types.action_type_artifact_details.serialize_cbor(
            value["output_artifact_details"]
        )
    )
    if "permissions" in value:
        import capo_codepipeline.types.action_type_permissions

        out["permissions"] = (
            capo_codepipeline.types.action_type_permissions.serialize_cbor(
                value["permissions"]
            )
        )
    if "properties" in value:
        import capo_codepipeline.types.action_type_properties

        out["properties"] = (
            capo_codepipeline.types.action_type_properties.serialize_cbor(
                value["properties"]
            )
        )
    if "urls" in value:
        import capo_codepipeline.types.action_type_urls

        out["urls"] = capo_codepipeline.types.action_type_urls.serialize_cbor(
            value["urls"]
        )
    return out


def deserialize_cbor(data: dict) -> ActionTypeDeclaration:
    out: ActionTypeDeclaration = {}  # type: ignore[typeddict-item]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("executor") is not None:
        import capo_codepipeline.types.action_type_executor

        out["executor"] = capo_codepipeline.types.action_type_executor.deserialize_cbor(
            data["executor"]
        )
    else:
        raise DeserializationError("ActionTypeDeclaration.executor required")
    if data.get("id") is not None:
        import capo_codepipeline.types.action_type_identifier

        out["id"] = capo_codepipeline.types.action_type_identifier.deserialize_cbor(
            data["id"]
        )
    else:
        raise DeserializationError("ActionTypeDeclaration.id required")
    if data.get("inputArtifactDetails") is not None:
        import capo_codepipeline.types.action_type_artifact_details

        out["input_artifact_details"] = (
            capo_codepipeline.types.action_type_artifact_details.deserialize_cbor(
                data["inputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "ActionTypeDeclaration.input_artifact_details required"
        )
    if data.get("outputArtifactDetails") is not None:
        import capo_codepipeline.types.action_type_artifact_details

        out["output_artifact_details"] = (
            capo_codepipeline.types.action_type_artifact_details.deserialize_cbor(
                data["outputArtifactDetails"]
            )
        )
    else:
        raise DeserializationError(
            "ActionTypeDeclaration.output_artifact_details required"
        )
    if data.get("permissions") is not None:
        import capo_codepipeline.types.action_type_permissions

        out["permissions"] = (
            capo_codepipeline.types.action_type_permissions.deserialize_cbor(
                data["permissions"]
            )
        )
    if data.get("properties") is not None:
        import capo_codepipeline.types.action_type_properties

        out["properties"] = (
            capo_codepipeline.types.action_type_properties.deserialize_cbor(
                data["properties"]
            )
        )
    if data.get("urls") is not None:
        import capo_codepipeline.types.action_type_urls

        out["urls"] = capo_codepipeline.types.action_type_urls.deserialize_cbor(
            data["urls"]
        )
    return out
