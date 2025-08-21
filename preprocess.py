import  json

def process_post(raw_file_path , processed_file_path = "data/processed_posts.json"):
    with open(raw_file_path , encoding= 'utf-8') as file :
        posts = json.load(file)
        enriched_posts = []
        for post in posts:
            metadata = extract_metadata(post['text'])

            post_with_matadata = post | metadata
            # | is a pipe operator that basically combines the content of metadata and the post

            enriched_posts.append(post_with_matadata)


        for en_post in enriched_posts:
                print(en_post)


def extract_metadata(post):
    return {
        'Line Count' : 10,
        'Language' : 'English',
        'tags' : ['Mental Health' , 'Motivation']
    }

if __name__ == "__main__":
    process_post("data/raw_posts.json" , "data/processed_posts.json")
