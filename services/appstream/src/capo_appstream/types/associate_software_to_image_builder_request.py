"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateSoftwareToImageBuilderRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.name
    import capo_appstream.types.string_list


class AssociateSoftwareToImageBuilderRequest(TypedDict, closed=True):
    image_builder_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the target image builder instance.</p>"""
    software_names: NotRequired["capo_appstream.types.string_list.StringList"]
    """<p>The list of license included applications to associate with the image builder.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateSoftwareToImageBuilderRequest) -> dict:
    out: dict = {}
    if "image_builder_name" in value:
        out["ImageBuilderName"] = value["image_builder_name"]
    if "software_names" in value:
        import capo_appstream.types.string_list

        out["SoftwareNames"] = capo_appstream.types.string_list.serialize_aws_json_1_1(
            value["software_names"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateSoftwareToImageBuilderRequest:
    out: AssociateSoftwareToImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilderName") is not None:
        out["image_builder_name"] = data["ImageBuilderName"]
    if data.get("SoftwareNames") is not None:
        import capo_appstream.types.string_list

        out["software_names"] = (
            capo_appstream.types.string_list.deserialize_aws_json_1_1(
                data["SoftwareNames"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateSoftwareToImageBuilderRequest) -> dict:
    out: dict = {}
    if "image_builder_name" in value:
        out["ImageBuilderName"] = value["image_builder_name"]
    if "software_names" in value:
        import capo_appstream.types.string_list

        out["SoftwareNames"] = capo_appstream.types.string_list.serialize_cbor(
            value["software_names"]
        )
    return out


def deserialize_cbor(data: dict) -> AssociateSoftwareToImageBuilderRequest:
    out: AssociateSoftwareToImageBuilderRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageBuilderName") is not None:
        out["image_builder_name"] = data["ImageBuilderName"]
    if data.get("SoftwareNames") is not None:
        import capo_appstream.types.string_list

        out["software_names"] = capo_appstream.types.string_list.deserialize_cbor(
            data["SoftwareNames"]
        )
    return out
