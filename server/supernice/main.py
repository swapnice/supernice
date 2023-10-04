#!/usr/bin/env python

import asyncio

import aiohttp
from fastapi import FastAPI

from .infrastructure.apis.main import test

app = FastAPI()


@app.get("/")
def read_root():
    print("----->jjj")
    MarketerPersona(" Swapnice is an superplatform for collectibles. Our foundation is inclusive, friendly and knowledgeable. Our impact is security, trust, and safety with collectibles. We use NFC technology to enhance items and our essence is to be the most secure platform to supercharge collectibles.", " An NFC tag in the middle of a screen with friends and family spending time together on a green pasture and a friendly neighborhood where people are engaging and trading collectibles like trading cards, sneakers, and clothes.")

    # return {"Hello": "World"}


async def fetch(session, url, method="GET", payload=None, headers=None):
    """fetch a single request with retries and exponential backoff"""
    retry_count = 0
    while retry_count < 2:
        try:
            if method == "GET":
                async with session.get(url, headers=headers) as response:
                    return await response.json()
            elif method == "POST":
                async with session.post(url, json=payload, headers=headers) as response:
                    return await response.json()
            elif method == "PUT":
                async with session.put(url, json=payload, headers=headers) as response:
                    return await response.json()
            elif method == "PATCH":
                async with session.patch(
                    url, json=payload, headers=headers
                ) as response:
                    return await response.json()
            elif method == "DELETE":
                async with session.delete(url, headers=headers) as response:
                    return await response.json()
            else:
                raise ValueError("Invalid method")
        except Exception as e:
            print(e)
            retry_count += 1
            await asyncio.sleep(2**retry_count)
    return None


async def process_batch(batch):
    """process a batch of requests"""
    async with aiohttp.ClientSession() as session:
        tasks = []
        for request in batch:
            print(request)
            task = asyncio.ensure_future(
                fetch(
                    session,
                    request["url"],
                    request["method"],
                    request["payload"],
                    request["headers"],
                )
            )
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses


def request_generator(batches):
    """Generator function that yields batches of requests"""
    try:
        print("----->")
        loop = asyncio.get_event_loop()

    except RuntimeError as e:
        #  print the RuntimeError
        if str(e).startswith("There is no current event loop in thread"):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        else:
            raise

    for batch in batches:
        yield loop.run_until_complete(process_batch(batch))


def MarketerPersona(brand_identity, img_description):
    prompt="You are a marketing master persona, embodying the foundational principles of Philip Kotler (Holistic, customer-centric marketing strategies ) , the advertising genius of David Ogilvy (Persuasive, research-based advertising copy) , the digital marketing expertise of Neil Patel (Effective, data-driven digital marketing), the compelling storytelling of Simon Sinek's (Inspirational brand storytelling) ’Start With Why,' the content marketing acumen of Ann Handley ( Engaging, valuable content creation )  and Joe Pulizzi ( Niche-focused content marketing strategy ) , the social media savviness of Gary Vaynerchuk ( Authentic, engaging social media presence ) and Mari Smith (Relationship-building through social platforms) , and the inbound marketing strategies of Brian Halligan (Attract, engage, delight inbound methodology).\nAnswer the Questions with the Inputs provided as the persona.\nINPUT:\n* Brand Identity: "+ brand_identity+"\n* Image Description: "+ img_description +"\nREQUEST:\nPlease craft three sentences based on the information provided to guide the transformation of the input image:\nOne: Can you articulate the emotional tone or activity that the image should convey to align with the brand identity?\nTwo: What stylistic modifications are necessary for the image to resonate with the brand’s aesthetic and visual language?\nThree: How can the image be adjusted to ensure consistency and cohesion with the overall brand identity?Output all Paragraphs together without separation in headers.\n"
    batches = [
        [
            {
                "url": "https://qe8c1zqxmsa3c6d9.us-east-1.aws.endpoints.huggingface.cloud",
                "method": "POST",
                "payload": {
                    "inputs": prompt,
                    "parameters": {
                        "max_new_tokens": 200,
                        "return_full_text": True,
                    },
                },
                "headers": {
                    "Cache-Control": "no-cache",
                    "Content-Type": "application/json",
                    "Authorization": "Bearer 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",
                },
            }
        ]
    ]

    for response in request_generator(batches):

        response = response[0]["generated_text"]
        # split a string on \n\n\n and only keep second half
        response = response.split("\n\n\n")[1]
        print("******"+response)

    pass
