"""Generated from Smithy shape ``com.amazonaws.finspace#CreateEnvironmentRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_finspace.errors import DeserializationError

if TYPE_CHECKING:
    import capo_finspace.types.data_bundle_arns
    import capo_finspace.types.description
    import capo_finspace.types.environment_name
    import capo_finspace.types.federation_mode
    import capo_finspace.types.federation_parameters
    import capo_finspace.types.kms_key_id
    import capo_finspace.types.superuser_parameters
    import capo_finspace.types.tag_map


class CreateEnvironmentRequest(TypedDict, closed=True):
    name: "capo_finspace.types.environment_name.EnvironmentName"
    """<p>The name of the FinSpace environment to be created.</p>"""
    description: NotRequired["capo_finspace.types.description.Description"]
    """<p>The description of the FinSpace environment to be created.</p>"""
    kms_key_id: NotRequired["capo_finspace.types.kms_key_id.KmsKeyId"]
    """<p>The KMS key id to encrypt your data in the FinSpace environment.</p>"""
    tags: NotRequired["capo_finspace.types.tag_map.TagMap"]
    """<p>Add tags to your FinSpace environment.</p>"""
    federation_mode: NotRequired["capo_finspace.types.federation_mode.FederationMode"]
    """<p>Authentication mode for the environment.</p> <ul> <li> <p> <code>FEDERATED</code> - Users access FinSpace through Single Sign On (SSO) via your Identity provider.</p> </li> <li> <p> <code>LOCAL</code> - Users access FinSpace via email and password managed within the FinSpace environment.</p> </li> </ul>"""
    federation_parameters: NotRequired[
        "capo_finspace.types.federation_parameters.FederationParameters"
    ]
    """<p>Configuration information when authentication mode is FEDERATED.</p>"""
    superuser_parameters: NotRequired[
        "capo_finspace.types.superuser_parameters.SuperuserParameters"
    ]
    """<p>Configuration information for the superuser.</p>"""
    data_bundles: NotRequired["capo_finspace.types.data_bundle_arns.DataBundleArns"]
    """<p>The list of Amazon Resource Names (ARN) of the data bundles to install. Currently supported data bundle ARNs:</p> <ul> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/capital-markets-sample</code> - Contains sample Capital Markets datasets, categories and controlled vocabularies.</p> </li> <li> <p> <code>arn:aws:finspace:${Region}::data-bundle/taq</code> (default) - Contains trades and quotes data in addition to sample Capital Markets data.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEnvironmentRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.serialize_json(value["tags"])
    if "federation_mode" in value:
        import capo_finspace.types.federation_mode

        out["federationMode"] = capo_finspace.types.federation_mode.serialize_json(
            value["federation_mode"]
        )
    if "federation_parameters" in value:
        import capo_finspace.types.federation_parameters

        out["federationParameters"] = (
            capo_finspace.types.federation_parameters.serialize_json(
                value["federation_parameters"]
            )
        )
    if "superuser_parameters" in value:
        import capo_finspace.types.superuser_parameters

        out["superuserParameters"] = (
            capo_finspace.types.superuser_parameters.serialize_json(
                value["superuser_parameters"]
            )
        )
    if "data_bundles" in value:
        import capo_finspace.types.data_bundle_arns

        out["dataBundles"] = capo_finspace.types.data_bundle_arns.serialize_json(
            value["data_bundles"]
        )
    return out


def deserialize_json(data: dict) -> CreateEnvironmentRequest:
    out: CreateEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateEnvironmentRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("tags") is not None:
        import capo_finspace.types.tag_map

        out["tags"] = capo_finspace.types.tag_map.deserialize_json(data["tags"])
    if data.get("federationMode") is not None:
        import capo_finspace.types.federation_mode

        out["federation_mode"] = capo_finspace.types.federation_mode.deserialize_json(
            data["federationMode"]
        )
    if data.get("federationParameters") is not None:
        import capo_finspace.types.federation_parameters

        out["federation_parameters"] = (
            capo_finspace.types.federation_parameters.deserialize_json(
                data["federationParameters"]
            )
        )
    if data.get("superuserParameters") is not None:
        import capo_finspace.types.superuser_parameters

        out["superuser_parameters"] = (
            capo_finspace.types.superuser_parameters.deserialize_json(
                data["superuserParameters"]
            )
        )
    if data.get("dataBundles") is not None:
        import capo_finspace.types.data_bundle_arns

        out["data_bundles"] = capo_finspace.types.data_bundle_arns.deserialize_json(
            data["dataBundles"]
        )
    return out


def redact_sensitive(value: CreateEnvironmentRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "superuser_parameters" in value:
        import capo_finspace.types.superuser_parameters

        out["superuser_parameters"] = (
            capo_finspace.types.superuser_parameters.redact_sensitive(
                value["superuser_parameters"]
            )
        )
    return out
