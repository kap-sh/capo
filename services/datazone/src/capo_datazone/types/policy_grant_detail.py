"""Generated from Smithy shape ``com.amazonaws.datazone#PolicyGrantDetail``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.add_to_project_member_pool_policy_grant_detail
    import capo_datazone.types.create_asset_type_policy_grant_detail
    import capo_datazone.types.create_domain_unit_policy_grant_detail
    import capo_datazone.types.create_environment_profile_policy_grant_detail
    import capo_datazone.types.create_form_type_policy_grant_detail
    import capo_datazone.types.create_glossary_policy_grant_detail
    import capo_datazone.types.create_project_from_project_profile_policy_grant_detail
    import capo_datazone.types.create_project_policy_grant_detail
    import capo_datazone.types.override_domain_unit_owners_policy_grant_detail
    import capo_datazone.types.override_project_owners_policy_grant_detail
    import capo_datazone.types.unit
    import capo_datazone.types.use_asset_type_policy_grant_detail


class _PolicyGrantDetail_createDomainUnit(TypedDict, closed=True):
    createDomainUnit: "capo_datazone.types.create_domain_unit_policy_grant_detail.CreateDomainUnitPolicyGrantDetail"


class _PolicyGrantDetail_overrideDomainUnitOwners(TypedDict, closed=True):
    overrideDomainUnitOwners: "capo_datazone.types.override_domain_unit_owners_policy_grant_detail.OverrideDomainUnitOwnersPolicyGrantDetail"


class _PolicyGrantDetail_addToProjectMemberPool(TypedDict, closed=True):
    addToProjectMemberPool: "capo_datazone.types.add_to_project_member_pool_policy_grant_detail.AddToProjectMemberPoolPolicyGrantDetail"


class _PolicyGrantDetail_overrideProjectOwners(TypedDict, closed=True):
    overrideProjectOwners: "capo_datazone.types.override_project_owners_policy_grant_detail.OverrideProjectOwnersPolicyGrantDetail"


class _PolicyGrantDetail_createGlossary(TypedDict, closed=True):
    createGlossary: "capo_datazone.types.create_glossary_policy_grant_detail.CreateGlossaryPolicyGrantDetail"


class _PolicyGrantDetail_createFormType(TypedDict, closed=True):
    createFormType: "capo_datazone.types.create_form_type_policy_grant_detail.CreateFormTypePolicyGrantDetail"


class _PolicyGrantDetail_createAssetType(TypedDict, closed=True):
    createAssetType: "capo_datazone.types.create_asset_type_policy_grant_detail.CreateAssetTypePolicyGrantDetail"


class _PolicyGrantDetail_createProject(TypedDict, closed=True):
    createProject: "capo_datazone.types.create_project_policy_grant_detail.CreateProjectPolicyGrantDetail"


class _PolicyGrantDetail_createEnvironmentProfile(TypedDict, closed=True):
    createEnvironmentProfile: "capo_datazone.types.create_environment_profile_policy_grant_detail.CreateEnvironmentProfilePolicyGrantDetail"


class _PolicyGrantDetail_delegateCreateEnvironmentProfile(TypedDict, closed=True):
    delegateCreateEnvironmentProfile: "capo_datazone.types.unit.Unit"


class _PolicyGrantDetail_createEnvironment(TypedDict, closed=True):
    createEnvironment: "capo_datazone.types.unit.Unit"


class _PolicyGrantDetail_createEnvironmentFromBlueprint(TypedDict, closed=True):
    createEnvironmentFromBlueprint: "capo_datazone.types.unit.Unit"


class _PolicyGrantDetail_createProjectFromProjectProfile(TypedDict, closed=True):
    createProjectFromProjectProfile: "capo_datazone.types.create_project_from_project_profile_policy_grant_detail.CreateProjectFromProjectProfilePolicyGrantDetail"


class _PolicyGrantDetail_useAssetType(TypedDict, closed=True):
    useAssetType: "capo_datazone.types.use_asset_type_policy_grant_detail.UseAssetTypePolicyGrantDetail"


PolicyGrantDetail: TypeAlias = (
    _PolicyGrantDetail_createDomainUnit
    | _PolicyGrantDetail_overrideDomainUnitOwners
    | _PolicyGrantDetail_addToProjectMemberPool
    | _PolicyGrantDetail_overrideProjectOwners
    | _PolicyGrantDetail_createGlossary
    | _PolicyGrantDetail_createFormType
    | _PolicyGrantDetail_createAssetType
    | _PolicyGrantDetail_createProject
    | _PolicyGrantDetail_createEnvironmentProfile
    | _PolicyGrantDetail_delegateCreateEnvironmentProfile
    | _PolicyGrantDetail_createEnvironment
    | _PolicyGrantDetail_createEnvironmentFromBlueprint
    | _PolicyGrantDetail_createProjectFromProjectProfile
    | _PolicyGrantDetail_useAssetType
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PolicyGrantDetail) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PolicyGrantDetail: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "createDomainUnit" in value:
        import capo_datazone.types.create_domain_unit_policy_grant_detail

        return {
            "createDomainUnit": capo_datazone.types.create_domain_unit_policy_grant_detail.serialize_json(
                value["createDomainUnit"]
            )
        }
    elif "overrideDomainUnitOwners" in value:
        import capo_datazone.types.override_domain_unit_owners_policy_grant_detail

        return {
            "overrideDomainUnitOwners": capo_datazone.types.override_domain_unit_owners_policy_grant_detail.serialize_json(
                value["overrideDomainUnitOwners"]
            )
        }
    elif "addToProjectMemberPool" in value:
        import capo_datazone.types.add_to_project_member_pool_policy_grant_detail

        return {
            "addToProjectMemberPool": capo_datazone.types.add_to_project_member_pool_policy_grant_detail.serialize_json(
                value["addToProjectMemberPool"]
            )
        }
    elif "overrideProjectOwners" in value:
        import capo_datazone.types.override_project_owners_policy_grant_detail

        return {
            "overrideProjectOwners": capo_datazone.types.override_project_owners_policy_grant_detail.serialize_json(
                value["overrideProjectOwners"]
            )
        }
    elif "createGlossary" in value:
        import capo_datazone.types.create_glossary_policy_grant_detail

        return {
            "createGlossary": capo_datazone.types.create_glossary_policy_grant_detail.serialize_json(
                value["createGlossary"]
            )
        }
    elif "createFormType" in value:
        import capo_datazone.types.create_form_type_policy_grant_detail

        return {
            "createFormType": capo_datazone.types.create_form_type_policy_grant_detail.serialize_json(
                value["createFormType"]
            )
        }
    elif "createAssetType" in value:
        import capo_datazone.types.create_asset_type_policy_grant_detail

        return {
            "createAssetType": capo_datazone.types.create_asset_type_policy_grant_detail.serialize_json(
                value["createAssetType"]
            )
        }
    elif "createProject" in value:
        import capo_datazone.types.create_project_policy_grant_detail

        return {
            "createProject": capo_datazone.types.create_project_policy_grant_detail.serialize_json(
                value["createProject"]
            )
        }
    elif "createEnvironmentProfile" in value:
        import capo_datazone.types.create_environment_profile_policy_grant_detail

        return {
            "createEnvironmentProfile": capo_datazone.types.create_environment_profile_policy_grant_detail.serialize_json(
                value["createEnvironmentProfile"]
            )
        }
    elif "delegateCreateEnvironmentProfile" in value:
        import capo_datazone.types.unit

        return {
            "delegateCreateEnvironmentProfile": capo_datazone.types.unit.serialize_json(
                value["delegateCreateEnvironmentProfile"]
            )
        }
    elif "createEnvironment" in value:
        import capo_datazone.types.unit

        return {
            "createEnvironment": capo_datazone.types.unit.serialize_json(
                value["createEnvironment"]
            )
        }
    elif "createEnvironmentFromBlueprint" in value:
        import capo_datazone.types.unit

        return {
            "createEnvironmentFromBlueprint": capo_datazone.types.unit.serialize_json(
                value["createEnvironmentFromBlueprint"]
            )
        }
    elif "createProjectFromProjectProfile" in value:
        import capo_datazone.types.create_project_from_project_profile_policy_grant_detail

        return {
            "createProjectFromProjectProfile": capo_datazone.types.create_project_from_project_profile_policy_grant_detail.serialize_json(
                value["createProjectFromProjectProfile"]
            )
        }
    elif "useAssetType" in value:
        import capo_datazone.types.use_asset_type_policy_grant_detail

        return {
            "useAssetType": capo_datazone.types.use_asset_type_policy_grant_detail.serialize_json(
                value["useAssetType"]
            )
        }
    else:
        raise SerializationError("PolicyGrantDetail: no variant present")


def deserialize_json(data: dict) -> PolicyGrantDetail:
    if data.get("createDomainUnit") is not None:
        import capo_datazone.types.create_domain_unit_policy_grant_detail

        return {
            "createDomainUnit": capo_datazone.types.create_domain_unit_policy_grant_detail.deserialize_json(
                data["createDomainUnit"]
            )
        }
    elif data.get("overrideDomainUnitOwners") is not None:
        import capo_datazone.types.override_domain_unit_owners_policy_grant_detail

        return {
            "overrideDomainUnitOwners": capo_datazone.types.override_domain_unit_owners_policy_grant_detail.deserialize_json(
                data["overrideDomainUnitOwners"]
            )
        }
    elif data.get("addToProjectMemberPool") is not None:
        import capo_datazone.types.add_to_project_member_pool_policy_grant_detail

        return {
            "addToProjectMemberPool": capo_datazone.types.add_to_project_member_pool_policy_grant_detail.deserialize_json(
                data["addToProjectMemberPool"]
            )
        }
    elif data.get("overrideProjectOwners") is not None:
        import capo_datazone.types.override_project_owners_policy_grant_detail

        return {
            "overrideProjectOwners": capo_datazone.types.override_project_owners_policy_grant_detail.deserialize_json(
                data["overrideProjectOwners"]
            )
        }
    elif data.get("createGlossary") is not None:
        import capo_datazone.types.create_glossary_policy_grant_detail

        return {
            "createGlossary": capo_datazone.types.create_glossary_policy_grant_detail.deserialize_json(
                data["createGlossary"]
            )
        }
    elif data.get("createFormType") is not None:
        import capo_datazone.types.create_form_type_policy_grant_detail

        return {
            "createFormType": capo_datazone.types.create_form_type_policy_grant_detail.deserialize_json(
                data["createFormType"]
            )
        }
    elif data.get("createAssetType") is not None:
        import capo_datazone.types.create_asset_type_policy_grant_detail

        return {
            "createAssetType": capo_datazone.types.create_asset_type_policy_grant_detail.deserialize_json(
                data["createAssetType"]
            )
        }
    elif data.get("createProject") is not None:
        import capo_datazone.types.create_project_policy_grant_detail

        return {
            "createProject": capo_datazone.types.create_project_policy_grant_detail.deserialize_json(
                data["createProject"]
            )
        }
    elif data.get("createEnvironmentProfile") is not None:
        import capo_datazone.types.create_environment_profile_policy_grant_detail

        return {
            "createEnvironmentProfile": capo_datazone.types.create_environment_profile_policy_grant_detail.deserialize_json(
                data["createEnvironmentProfile"]
            )
        }
    elif data.get("delegateCreateEnvironmentProfile") is not None:
        import capo_datazone.types.unit

        return {
            "delegateCreateEnvironmentProfile": capo_datazone.types.unit.deserialize_json(
                data["delegateCreateEnvironmentProfile"]
            )
        }
    elif data.get("createEnvironment") is not None:
        import capo_datazone.types.unit

        return {
            "createEnvironment": capo_datazone.types.unit.deserialize_json(
                data["createEnvironment"]
            )
        }
    elif data.get("createEnvironmentFromBlueprint") is not None:
        import capo_datazone.types.unit

        return {
            "createEnvironmentFromBlueprint": capo_datazone.types.unit.deserialize_json(
                data["createEnvironmentFromBlueprint"]
            )
        }
    elif data.get("createProjectFromProjectProfile") is not None:
        import capo_datazone.types.create_project_from_project_profile_policy_grant_detail

        return {
            "createProjectFromProjectProfile": capo_datazone.types.create_project_from_project_profile_policy_grant_detail.deserialize_json(
                data["createProjectFromProjectProfile"]
            )
        }
    elif data.get("useAssetType") is not None:
        import capo_datazone.types.use_asset_type_policy_grant_detail

        return {
            "useAssetType": capo_datazone.types.use_asset_type_policy_grant_detail.deserialize_json(
                data["useAssetType"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PolicyGrantDetail: no recognized variant key")
