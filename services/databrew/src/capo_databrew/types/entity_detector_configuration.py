"""Generated from Smithy shape ``com.amazonaws.databrew#EntityDetectorConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_databrew.types.allowed_statistic_list
    import capo_databrew.types.entity_type_list


class EntityDetectorConfiguration(TypedDict, closed=True):
    entity_types: "capo_databrew.types.entity_type_list.EntityTypeList"
    """<p>Entity types to detect. Can be any of the following:</p> <ul> <li> <p>USA_SSN</p> </li> <li> <p>EMAIL</p> </li> <li> <p>USA_ITIN</p> </li> <li> <p>USA_PASSPORT_NUMBER</p> </li> <li> <p>PHONE_NUMBER</p> </li> <li> <p>USA_DRIVING_LICENSE</p> </li> <li> <p>BANK_ACCOUNT</p> </li> <li> <p>CREDIT_CARD</p> </li> <li> <p>IP_ADDRESS</p> </li> <li> <p>MAC_ADDRESS</p> </li> <li> <p>USA_DEA_NUMBER</p> </li> <li> <p>USA_HCPCS_CODE</p> </li> <li> <p>USA_NATIONAL_PROVIDER_IDENTIFIER</p> </li> <li> <p>USA_NATIONAL_DRUG_CODE</p> </li> <li> <p>USA_HEALTH_INSURANCE_CLAIM_NUMBER</p> </li> <li> <p>USA_MEDICARE_BENEFICIARY_IDENTIFIER</p> </li> <li> <p>USA_CPT_CODE</p> </li> <li> <p>PERSON_NAME</p> </li> <li> <p>DATE</p> </li> </ul> <p>The Entity type group USA_ALL is also supported, and includes all of the above entity types except PERSON_NAME and DATE.</p>"""
    allowed_statistics: NotRequired[
        "capo_databrew.types.allowed_statistic_list.AllowedStatisticList"
    ]
    """<p>Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EntityDetectorConfiguration) -> dict:
    out: dict = {}
    import capo_databrew.types.entity_type_list

    out["EntityTypes"] = capo_databrew.types.entity_type_list.serialize_json(
        value["entity_types"]
    )
    if "allowed_statistics" in value:
        import capo_databrew.types.allowed_statistic_list

        out["AllowedStatistics"] = (
            capo_databrew.types.allowed_statistic_list.serialize_json(
                value["allowed_statistics"]
            )
        )
    return out


def deserialize_json(data: dict) -> EntityDetectorConfiguration:
    out: EntityDetectorConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("EntityTypes") is not None:
        import capo_databrew.types.entity_type_list

        out["entity_types"] = capo_databrew.types.entity_type_list.deserialize_json(
            data["EntityTypes"]
        )
    else:
        out["entity_types"] = []
    if data.get("AllowedStatistics") is not None:
        import capo_databrew.types.allowed_statistic_list

        out["allowed_statistics"] = (
            capo_databrew.types.allowed_statistic_list.deserialize_json(
                data["AllowedStatistics"]
            )
        )
    return out
