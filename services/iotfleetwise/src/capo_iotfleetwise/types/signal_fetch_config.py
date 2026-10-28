"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#SignalFetchConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_iotfleetwise.errors import DeserializationError, SerializationError
from capo_iotfleetwise.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_iotfleetwise.types.condition_based_signal_fetch_config
    import capo_iotfleetwise.types.time_based_signal_fetch_config


class SignalFetchConfigTimeBasedMember(TypedDict, closed=True):
    timeBased: "capo_iotfleetwise.types.time_based_signal_fetch_config.TimeBasedSignalFetchConfig"


class SignalFetchConfigConditionBasedMember(TypedDict, closed=True):
    conditionBased: "capo_iotfleetwise.types.condition_based_signal_fetch_config.ConditionBasedSignalFetchConfig"


SignalFetchConfig: TypeAlias = (
    SignalFetchConfigTimeBasedMember
    | SignalFetchConfigConditionBasedMember
    | UnknownUnionMember
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SignalFetchConfig) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SignalFetchConfig: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "timeBased" in value:
        import capo_iotfleetwise.types.time_based_signal_fetch_config

        return {
            "timeBased": capo_iotfleetwise.types.time_based_signal_fetch_config.serialize_aws_json_1_0(
                value["timeBased"]
            )
        }
    elif "conditionBased" in value:
        import capo_iotfleetwise.types.condition_based_signal_fetch_config

        return {
            "conditionBased": capo_iotfleetwise.types.condition_based_signal_fetch_config.serialize_aws_json_1_0(
                value["conditionBased"]
            )
        }
    else:
        raise SerializationError("SignalFetchConfig: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SignalFetchConfig:
    if data.get("timeBased") is not None:
        import capo_iotfleetwise.types.time_based_signal_fetch_config

        return {
            "timeBased": capo_iotfleetwise.types.time_based_signal_fetch_config.deserialize_aws_json_1_0(
                data["timeBased"]
            )
        }
    elif data.get("conditionBased") is not None:
        import capo_iotfleetwise.types.condition_based_signal_fetch_config

        return {
            "conditionBased": capo_iotfleetwise.types.condition_based_signal_fetch_config.deserialize_aws_json_1_0(
                data["conditionBased"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SignalFetchConfig: no recognized variant key")


def redact_sensitive(value: SignalFetchConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "conditionBased" in value:
        import capo_iotfleetwise.types.condition_based_signal_fetch_config

        out["conditionBased"] = (
            capo_iotfleetwise.types.condition_based_signal_fetch_config.redact_sensitive(
                value["conditionBased"]
            )
        )
    return out
