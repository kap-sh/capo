"""Generated from Smithy shape ``com.amazonaws.acm#GeneralName``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_acm.errors import DeserializationError, SerializationError
from capo_acm.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_acm.types.distinguished_name
    import capo_acm.types.other_name
    import capo_acm.types.string


class GeneralNameDirectoryNameMember(TypedDict, closed=True):
    DirectoryName: "capo_acm.types.distinguished_name.DistinguishedName"


class GeneralNameDnsNameMember(TypedDict, closed=True):
    DnsName: "capo_acm.types.string.String"


class GeneralNameIpAddressMember(TypedDict, closed=True):
    IpAddress: "capo_acm.types.string.String"


class GeneralNameOtherNameMember(TypedDict, closed=True):
    OtherName: "capo_acm.types.other_name.OtherName"


class GeneralNameRegisteredIdMember(TypedDict, closed=True):
    RegisteredId: "capo_acm.types.string.String"


class GeneralNameRfc822NameMember(TypedDict, closed=True):
    Rfc822Name: "capo_acm.types.string.String"


class GeneralNameUniformResourceIdentifierMember(TypedDict, closed=True):
    UniformResourceIdentifier: "capo_acm.types.string.String"


GeneralName: TypeAlias = (
    GeneralNameDirectoryNameMember
    | GeneralNameDnsNameMember
    | GeneralNameIpAddressMember
    | GeneralNameOtherNameMember
    | GeneralNameRegisteredIdMember
    | GeneralNameRfc822NameMember
    | GeneralNameUniformResourceIdentifierMember
    | UnknownUnionMember
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GeneralName) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GeneralName: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "DirectoryName" in value:
        import capo_acm.types.distinguished_name

        return {
            "DirectoryName": capo_acm.types.distinguished_name.serialize_aws_json_1_1(
                value["DirectoryName"]
            )
        }
    elif "DnsName" in value:
        return {"DnsName": value["DnsName"]}
    elif "IpAddress" in value:
        return {"IpAddress": value["IpAddress"]}
    elif "OtherName" in value:
        import capo_acm.types.other_name

        return {
            "OtherName": capo_acm.types.other_name.serialize_aws_json_1_1(
                value["OtherName"]
            )
        }
    elif "RegisteredId" in value:
        return {"RegisteredId": value["RegisteredId"]}
    elif "Rfc822Name" in value:
        return {"Rfc822Name": value["Rfc822Name"]}
    elif "UniformResourceIdentifier" in value:
        return {"UniformResourceIdentifier": value["UniformResourceIdentifier"]}
    else:
        raise SerializationError("GeneralName: no variant present")


def deserialize_aws_json_1_1(data: dict) -> GeneralName:
    if data.get("DirectoryName") is not None:
        import capo_acm.types.distinguished_name

        return {
            "DirectoryName": capo_acm.types.distinguished_name.deserialize_aws_json_1_1(
                data["DirectoryName"]
            )
        }
    elif data.get("DnsName") is not None:
        return {"DnsName": data["DnsName"]}
    elif data.get("IpAddress") is not None:
        return {"IpAddress": data["IpAddress"]}
    elif data.get("OtherName") is not None:
        import capo_acm.types.other_name

        return {
            "OtherName": capo_acm.types.other_name.deserialize_aws_json_1_1(
                data["OtherName"]
            )
        }
    elif data.get("RegisteredId") is not None:
        return {"RegisteredId": data["RegisteredId"]}
    elif data.get("Rfc822Name") is not None:
        return {"Rfc822Name": data["Rfc822Name"]}
    elif data.get("UniformResourceIdentifier") is not None:
        return {"UniformResourceIdentifier": data["UniformResourceIdentifier"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GeneralName: no recognized variant key")
