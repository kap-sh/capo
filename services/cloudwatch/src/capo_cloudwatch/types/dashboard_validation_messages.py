"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DashboardValidationMessages``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.dashboard_validation_message

DashboardValidationMessages: TypeAlias = list[
    "capo_cloudwatch.types.dashboard_validation_message.DashboardValidationMessage"
]


# --- awsQuery ser/de ---
def serialize_query(
    value: DashboardValidationMessages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.dashboard_validation_message

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.dashboard_validation_message.serialize_query(
            item, pairs, f"{prefix}.member.{n}"
        )


def deserialize_query(el: Element) -> DashboardValidationMessages:
    import capo_cloudwatch.types.dashboard_validation_message

    out: DashboardValidationMessages = []
    for child in el.findall("member"):
        out.append(
            capo_cloudwatch.types.dashboard_validation_message.deserialize_query(child)
        )
    return out


def serialize_query_flat(
    value: DashboardValidationMessages, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_cloudwatch.types.dashboard_validation_message

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_cloudwatch.types.dashboard_validation_message.serialize_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_query_flat(parent: Element, tag: str) -> DashboardValidationMessages:
    import capo_cloudwatch.types.dashboard_validation_message

    out: DashboardValidationMessages = []
    for child in parent.findall(tag):
        out.append(
            capo_cloudwatch.types.dashboard_validation_message.deserialize_query(child)
        )
    return out


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DashboardValidationMessages) -> list:
    import capo_cloudwatch.types.dashboard_validation_message

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.dashboard_validation_message.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> DashboardValidationMessages:
    import capo_cloudwatch.types.dashboard_validation_message

    out: DashboardValidationMessages = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.dashboard_validation_message.deserialize_aws_json_1_0(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DashboardValidationMessages) -> list:
    import capo_cloudwatch.types.dashboard_validation_message

    out: list = []
    for item in value:
        out.append(
            capo_cloudwatch.types.dashboard_validation_message.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> DashboardValidationMessages:
    import capo_cloudwatch.types.dashboard_validation_message

    out: DashboardValidationMessages = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_cloudwatch.types.dashboard_validation_message.deserialize_cbor(item)
        )
    return out
