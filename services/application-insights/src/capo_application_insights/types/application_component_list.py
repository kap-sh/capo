"""Generated from Smithy shape ``com.amazonaws.applicationinsights#ApplicationComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_application_insights.types.application_component

ApplicationComponentList: TypeAlias = list[
    "capo_application_insights.types.application_component.ApplicationComponent"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationComponentList) -> list:
    import capo_application_insights.types.application_component

    out: list = []
    for item in value:
        out.append(
            capo_application_insights.types.application_component.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ApplicationComponentList:
    import capo_application_insights.types.application_component

    out: ApplicationComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_insights.types.application_component.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ApplicationComponentList) -> list:
    import capo_application_insights.types.application_component

    out: list = []
    for item in value:
        out.append(
            capo_application_insights.types.application_component.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ApplicationComponentList:
    import capo_application_insights.types.application_component

    out: ApplicationComponentList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_application_insights.types.application_component.deserialize_cbor(item)
        )
    return out
