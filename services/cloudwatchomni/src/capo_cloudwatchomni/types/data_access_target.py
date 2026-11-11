"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#DataAccessTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.data_access_action_list


class DataAccessTarget(TypedDict, closed=True):
    actions: "capo_cloudwatchomni.types.data_access_action_list.DataAccessActionList"
    """The actions of one service, each with its service prefix, for example "logs:StartQuery"."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DataAccessTarget) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.data_access_action_list

    out["actions"] = capo_cloudwatchomni.types.data_access_action_list.serialize_cbor(
        value["actions"]
    )
    return out


def deserialize_cbor(data: dict) -> DataAccessTarget:
    out: DataAccessTarget = {}  # type: ignore[typeddict-item]
    if data.get("actions") is not None:
        import capo_cloudwatchomni.types.data_access_action_list

        out["actions"] = (
            capo_cloudwatchomni.types.data_access_action_list.deserialize_cbor(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    return out
