from pathlib import Path
from src.article import parse_url

if __name__ == "__main__":
    urls = [
        "https://www.boursorama.com/bourse/actualites/net-rebond-du-cac-40-apres-le-premier-tour-des-legislatives-7be70d803561a5e8f62efcc8da9a513f",
        "https://www.tf1info.fr/elections/resultats-elections-legislatives-2024-l-extreme-droite-rassemblement-national-marine-le-pen-en-tete-un-choc-et-une-nouvelle-ere-pour-la-presse-etrangere-2306513.html",
        "https://www.liberation.fr/politique/elections/resultats-des-legislatives-2024-chez-les-dissidents-insoumis-alexis-corbiere-sen-sort-raquel-garrido-au-rupteur-20240701_FDKFKBN7C5DXNGTVPFY52O5XJM/",
    ]
    for url_id,url in enumerate(urls):
        article = parse_url(url)
        
        print("Title:")
        print(article.title)
        print()
        print("Content:")
        print(article.content)
        print("##########################""")
        Path(f"tests/data/{url_id:02d}_test_article.json").write_text(article.to_json(indent=4))