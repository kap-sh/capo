"""Generated from Smithy shape ``com.amazonaws.healthlake#CreateDataTransformationProfileSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_healthlake.errors import DeserializationError, SerializationError
from capo_healthlake.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_healthlake.types.existing_versioned_profile_source
    import capo_healthlake.types.profile_mapping_source
    import capo_healthlake.types.sample_data_source
    import capo_healthlake.types.starter_profile_source


class CreateDataTransformationProfileSourceStarterProfileMember(TypedDict, closed=True):
    StarterProfile: "capo_healthlake.types.starter_profile_source.StarterProfileSource"


class CreateDataTransformationProfileSourceExistingVersionedProfileIdMember(
    TypedDict, closed=True
):
    ExistingVersionedProfileId: "capo_healthlake.types.existing_versioned_profile_source.ExistingVersionedProfileSource"


class CreateDataTransformationProfileSourceProfileMappingMember(TypedDict, closed=True):
    ProfileMapping: "capo_healthlake.types.profile_mapping_source.ProfileMappingSource"


class CreateDataTransformationProfileSourceSampleDataMember(TypedDict, closed=True):
    SampleData: "capo_healthlake.types.sample_data_source.SampleDataSource"


CreateDataTransformationProfileSource: TypeAlias = (
    CreateDataTransformationProfileSourceStarterProfileMember
    | CreateDataTransformationProfileSourceExistingVersionedProfileIdMember
    | CreateDataTransformationProfileSourceProfileMappingMember
    | CreateDataTransformationProfileSourceSampleDataMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateDataTransformationProfileSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"CreateDataTransformationProfileSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "StarterProfile" in value:
        import capo_healthlake.types.starter_profile_source

        return {
            "StarterProfile": capo_healthlake.types.starter_profile_source.serialize_aws_json_1_0(
                value["StarterProfile"]
            )
        }
    elif "ExistingVersionedProfileId" in value:
        import capo_healthlake.types.existing_versioned_profile_source

        return {
            "ExistingVersionedProfileId": capo_healthlake.types.existing_versioned_profile_source.serialize_aws_json_1_0(
                value["ExistingVersionedProfileId"]
            )
        }
    elif "ProfileMapping" in value:
        import capo_healthlake.types.profile_mapping_source

        return {
            "ProfileMapping": capo_healthlake.types.profile_mapping_source.serialize_aws_json_1_0(
                value["ProfileMapping"]
            )
        }
    elif "SampleData" in value:
        import capo_healthlake.types.sample_data_source

        return {
            "SampleData": capo_healthlake.types.sample_data_source.serialize_aws_json_1_0(
                value["SampleData"]
            )
        }
    else:
        raise SerializationError(
            "CreateDataTransformationProfileSource: no variant present"
        )


def deserialize_aws_json_1_0(data: dict) -> CreateDataTransformationProfileSource:
    if data.get("StarterProfile") is not None:
        import capo_healthlake.types.starter_profile_source

        return {
            "StarterProfile": capo_healthlake.types.starter_profile_source.deserialize_aws_json_1_0(
                data["StarterProfile"]
            )
        }
    elif data.get("ExistingVersionedProfileId") is not None:
        import capo_healthlake.types.existing_versioned_profile_source

        return {
            "ExistingVersionedProfileId": capo_healthlake.types.existing_versioned_profile_source.deserialize_aws_json_1_0(
                data["ExistingVersionedProfileId"]
            )
        }
    elif data.get("ProfileMapping") is not None:
        import capo_healthlake.types.profile_mapping_source

        return {
            "ProfileMapping": capo_healthlake.types.profile_mapping_source.deserialize_aws_json_1_0(
                data["ProfileMapping"]
            )
        }
    elif data.get("SampleData") is not None:
        import capo_healthlake.types.sample_data_source

        return {
            "SampleData": capo_healthlake.types.sample_data_source.deserialize_aws_json_1_0(
                data["SampleData"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "CreateDataTransformationProfileSource: no recognized variant key"
        )


def redact_sensitive(value: CreateDataTransformationProfileSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "ProfileMapping" in value:
        out["ProfileMapping"] = "*** Sensitive Data Redacted ***"
    return out
