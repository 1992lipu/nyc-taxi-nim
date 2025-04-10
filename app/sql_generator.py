from openai import OpenAI
from config import  NIM_API_KEY

def generate_sql(query: str, schema: str) -> str:
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key="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"
    )

    completion = client.chat.completions.create(
        model="nvidia/mistral-nemo-minitron-8b-8k-instruct",
        messages=[
            {"role": "system", "content": ""
                                          "Generate only the SQL query and nothing else. "
                                          "DO NOT ADD ANY COMMENTS OR DESCRIPTIONS. "
                                          "TABLE NAME IS 'nyc_taxi_data'"
                                          "SEND DUCKDB COMPATIBLE SQL QUERY"
                                          "TABLE HAS ONLY 2016 DATA"},
            {"role": "user", "content": f"Generate an SQL query with the following query: {query}, table schema is: {schema}"}
        ],
        temperature=0.5,
        top_p=1,
        max_tokens=1024,
        stream=True
    )

    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content is not None:
            response += chunk.choices[0].delta.content

    return response