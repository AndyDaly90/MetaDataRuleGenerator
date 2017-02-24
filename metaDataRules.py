from switch import Switch
from operator import is_not
from functools import partial


class MetaDataRules:
    def __init__(self):
        pass

    @staticmethod
    def setValue(form_id, dest_field_id, set_val):
        rule = "SetValue[[-SEP-]]" + str(form_id) + "[[-SEP-]]" \
               + str(dest_field_id) + "[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]][[-SEP-]]" \
               + str(set_val) + "[[-SEP-]][[" \
                                "-SEP-]][[" \
                                "-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def concat(form_id, dest_field_id, first_field_id, concat_value, second_field_id):
        rule = "Concat[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(dest_field_id) + "[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(first_field_id) + "[[-SEP-]][[-SEP-]]" \
               + str(form_id) + "[[-SEP-]][[-SEP-]]" \
               + str(concat_value) + "[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(second_field_id) + "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def delete(form_id, field_id):
        rule = "Delete[[-SEP-]]" \
               + str(form_id) + "[[-SEP-]]" \
               + str(field_id) + "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[" \
                                 "-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def stringToDate(destination_field_id, source_field_id):
        rule = "NumberStringToDate[[-SEP-]]" \
               + str(destination_field_id) + "[[-SEP-]]" \
               + str(source_field_id) + "[[-SEP-]]True[[-SEP-]][" \
                                        "[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[" \
                                        "-SEP-]][[-SEP-]][[" \
                                        "-SEP-]][[-SEP-]][[-SEP-]]"
        return rule

    @staticmethod
    def validate_BIC_IBAN(bic_iban, source_id, destination_id):
        with Switch(bic_iban) as case:
            if case('BIC'):
                rule = "IbanBicValidation[[-SEP-]]BIC[[-SEP-]]" \
                       + str(source_id) + "[[-SEP-]]" \
                       + str(destination_id) + "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]" \
                                               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
            if case('IBAN'):
                rule = "IbanBicValidation[[-SEP-]]IBAN[[-SEP-]]" \
                       + str(source_id) + "[[-SEP-]]" \
                       + str(destination_id) + "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]" \
                                               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"
            return rule

    @staticmethod
    def crossDbInsert(source_id, source_form, source_field_values,
                      destination_id, destination_field_values):
        source_str = ""
        dest_str = ""

        for i in range(len(source_field_values)):
            if i == len(source_field_values) - 1:
                source_str += source_field_values[i]
            else:
                source_str += source_field_values[i] + ","

        for i in range(len(destination_field_values)):
            if i == len(destination_field_values) - 1:
                dest_str += destination_field_values[i]
            else:
                dest_str += destination_field_values[i] + ","

        rule = "CrossDatabase_Insert" \
               "[[-SEP-]]SOURCE_FORM_ID" \
               "[[-SEP-]]SOURCE_FORM" \
               "[[-SEP-]]SOURCE_FORM_ID" \
               "[[-SEP-]]SOURCE_FIELD_VALUES" \
               "[[-SEP-]]" \
               "[[-SEP-]]DEST_FORM_ID" \
               "[[-SEP-]]DESTINATION_FIELD_VALUES" \
               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]" \
               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"

        rule = rule.replace("SOURCE_FORM_ID", source_id) \
            .replace("SOURCE_FORM", source_form) \
            .replace("SOURCE_FIELD_VALUES", source_str) \
            .replace("DEST_FORM_ID", destination_id) \
            .replace("DESTINATION_FIELD_VALUES", dest_str)
        return rule

    @staticmethod
    def crossDbRetrieval(destination_ids, source_form_id, source_ids, source_ids_match, destination_vals_match):
        destination_ids_str = ""
        source_ids_str = ""
        source_ids_match_str = ""
        destination_vals_match_str = ""

        source_form_id = str(source_form_id[0])

        def removeNone(_list):
            _list = filter(partial(is_not, None), _list)
            return _list

        destination_ids = removeNone(destination_ids)
        source_ids = removeNone(source_ids)

        for i in range(len(destination_ids)):
            if i == len(destination_ids) - 1:
                destination_ids_str += destination_ids[i]
            else:
                destination_ids_str += destination_ids[i] + ","
        for i in range(len(source_ids)):
            if i == len(source_ids) - 1:
                source_ids_str += source_ids[i]
            else:
                source_ids_str += source_ids[i] + ","
        for i in range(len(source_ids_match)):
            if i == len(source_ids_match) - 1:
                source_ids_match_str += source_ids_match[i]
            else:
                source_ids_match_str += source_ids_match[i] + ","
        for i in range(len(destination_vals_match)):
            if i == len(destination_vals_match) - 1:
                destination_vals_match_str += destination_vals_match[i]
            else:
                destination_vals_match_str += destination_vals_match[i] + ","

        rule = "CrossDatabase_Retrieval_Dynamic[[-SEP-]]Destination_Ids[[-SEP-]]Source_form_id[[" \
               "-SEP-]]Source_Ids[[-SEP-]]Source_match[[-SEP-]]Destination_match" \
               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]" \
               "[[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]"

        rule = rule.replace("Destination_Ids", destination_ids_str) \
            .replace("Source_form_id", source_form_id) \
            .replace("Source_Ids", source_ids_str) \
            .replace("Source_match", source_ids_match_str) \
            .replace("Destination_match", destination_vals_match_str)
        return rule

    @staticmethod
    def customFileOutput(source_headers, source_field_ids, source_id, export_title, file_path, variable):

        source_head_str = ""
        source_id_str = ""

        for i in range(len(source_headers)):
            if i == len(source_headers) - 1:
                source_head_str += source_headers[i]
            else:
                source_head_str += source_headers[i] + ","

        for i in range(len(source_field_ids)):
            if i == len(source_field_ids) - 1:
                source_id_str += source_field_ids[i]
            else:
                source_id_str += source_field_ids[i] + ","

        with Switch(variable) as case:
            if case('TXT'):
                rule = "Output_CustomFileOutput[[-SEP-]]FORM_ID[[-SEP-]]HEADERS[[-SEP-]]FIELD_IDS[[-SEP-]]SFTP[[" \
                       "-SEP-]]TITLE[[-SEP-]]|[[-SEP-]][[-SEP-]]\\[[-SEP-]]\n[[-SEP-]]1000000000[[" \
                       "-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]FILEPATH[[-SEP-]][[-SEP-]][[-SEP-]]"

                rule = rule.encode('string-escape') \
                    .replace("FORM_ID", str(source_id)) \
                    .replace("HEADERS", str(source_head_str)) \
                    .replace("FIELD_IDS", str(source_id_str)) \
                    .replace("TITLE", str(export_title)) \
                    .replace("FILEPATH", str(file_path))

            if case('CSV'):
                rule = "Output_CustomFileOutput[[-SEP-]]FORM_ID[[-SEP-]]HEADERS[[-SEP-]]FIELD_IDS[[-SEP-]]SFTP[[" \
                       "-SEP-]]TITLE[[-SEP-]],[[-SEP-]]DoubleComma[[-SEP-]]\\[[-SEP-]]\n[[-SEP-]]1000000000[[" \
                       "-SEP-]][[-SEP-]][[-SEP-]][[-SEP-]]FILEPATH[[-SEP-]][[-SEP-]][[-SEP-]]"

                rule = rule.encode('string-escape') \
                    .replace("FORM_ID", str(source_id)) \
                    .replace("HEADERS", str(source_head_str)) \
                    .replace("FIELD_IDS", str(source_id_str)) \
                    .replace("TITLE", str(export_title)) \
                    .replace("FILEPATH", str(file_path))
        return rule
