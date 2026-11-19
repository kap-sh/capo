"""Generated from Smithy shape ``com.amazonaws.ec2#AdditionalKeyExchangeMethodsList``."""

from typing import TYPE_CHECKING, TypeAlias

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.additional_key_exchange_methods_list_value

AdditionalKeyExchangeMethodsList: TypeAlias = list[
    "capo_ec2.types.additional_key_exchange_methods_list_value.AdditionalKeyExchangeMethodsListValue"
]


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: AdditionalKeyExchangeMethodsList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if not value:
        return
    for n, item in enumerate(value, 1):
        import capo_ec2.types.additional_key_exchange_methods_list_value

        capo_ec2.types.additional_key_exchange_methods_list_value.serialize_ec2_query(
            item, pairs, f"{prefix}.{n}"
        )


def deserialize_ec2_query(el: Element) -> AdditionalKeyExchangeMethodsList:
    import capo_ec2.types.additional_key_exchange_methods_list_value

    out: AdditionalKeyExchangeMethodsList = []
    for child in el.findall("item"):
        out.append(
            capo_ec2.types.additional_key_exchange_methods_list_value.deserialize_ec2_query(
                child
            )
        )
    return out


def deserialize_ec2_query_flat(
    parent: Element, tag: str
) -> AdditionalKeyExchangeMethodsList:
    import capo_ec2.types.additional_key_exchange_methods_list_value

    out: AdditionalKeyExchangeMethodsList = []
    for child in parent.findall(tag):
        out.append(
            capo_ec2.types.additional_key_exchange_methods_list_value.deserialize_ec2_query(
                child
            )
        )
    return out
