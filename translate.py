# from transformers import MarianMTModel, MarianTokenizer

# loaded_models = {}

# model_name = "Helsinki-NLP/opus-mt-en-fr"
# def get_model(source_lang, target_lang):

#     model_name = f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}"

#     if model_name not in loaded_models:

#         tokenizer = MarianTokenizer.from_pretrained(model_name)

#         model = MarianMTModel.from_pretrained(model_name)

#         loaded_models[model_name] = (tokenizer, model)

#     return loaded_models[model_name]


# def translate_text(text, source_lang, target_lang):

#     tokenizer, model = get_model(source_lang, target_lang)

#     inputs = tokenizer(
#         text,
#         return_tensors="pt",
#         padding=True
#     )

#     translated = model.generate(**inputs)

#     output = tokenizer.decode(
#         translated[0],
#         skip_special_tokens=True
#     )

#     return output

from deep_translator import GoogleTranslator

def translate_text(text, source_lang, target_lang):

    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)

    return translated

def get_supported_languages():

    return GoogleTranslator().get_supported_languages(
        as_dict=True
    )