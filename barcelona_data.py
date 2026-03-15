# Data Barcelona - Hidden Gems & Local Spots
barcelona_locations = {
    "gracia": {
        "name": "Gràcia - Bohemian Neighborhood",
        "category": "neighborhood",
        "description": "Dulu kota terpisah, sekarang district bohemian dengan plaza-plaza kecil, toko independen, dan vibe artistik. Jauh dari keramaian turis.",
        "neighbors": ["carrer_verdi", "plaça_sol", "park_guell"]
    },
    
    "carrer_verdi": {
        "name": "Carrer Verdi",
        "category": "street",
        "description": "Jalan utama di Gràcia dengan bioskop indie (Verdi Cinema), tapas bar, dan butik lokal. Tempat nongkrong favorit warga lokal.",
        "neighbors": ["gracia", "plaça_sol"]
    },
    
    "plaça_sol": {
        "name": "Plaça del Sol",
        "category": "square",
        "description": "Plaza paling hidup di Gràcia. Dipenuhi bar dan kafe outdoor. Ramai sampai larut malam, terutama akhir pekan.",
        "neighbors": ["gracia", "carrer_verdi"]
    },
    
    "el_raval": {
        "name": "El Raval - Multicultural Heart",
        "category": "neighborhood",
        "description": "Dulu daerah merah, sekarang melting pot budaya dengan imigran dari seluruh dunia. Penuh restoran Pakistan, India, Filipina, dan seni jalanan.",
        "neighbors": ["macba", "la_rambla_del_raval", "boqueria"]
    },
    
    "macba": {
        "name": "MACBA - Museum of Contemporary Art",
        "category": "museum",
        "description": "Museum seni kontemporer dengan plaza luas yang jadi tempat nongkrong skater anak muda Barcelona.",
        "neighbors": ["el_raval", "la_rambla_del_raval"]
    },
    
    "la_rambla_del_raval": {
        "name": "Rambla del Raval",
        "category": "street",
        "description": "Jalan lebar di Raval dengan patung kucing raksasa (El Gat) karya Botero. Tempat nongkrong dan makan enak.",
        "neighbors": ["el_raval", "macba"]
    },
    
    "boqueria": {
        "name": "La Boqueria - Hidden Morning",
        "category": "market",
        "description": "Pasar terkenal, tapi datanglah pagi-pagi (sebelum jam 9) untuk merasakan suasana pasar tradisional tanpa turis. Coba jus dan makanan segar.",
        "neighbors": ["el_raval", "la_rambla"]
    },
    
    "poble_sec": {
        "name": "Poble Sec - Theater District",
        "category": "neighborhood",
        "description": "Daerah di kaki bukit Montjuïc. Penuh teater, bar tapas, dan restoran lokal. Jauh dari keramaian turis.",
        "neighbors": ["carrer_blai", "montjuic"]
    },
    
    "carrer_blai": {
        "name": "Carrer Blai - Pintxos Street",
        "category": "street",
        "description": "Jalan pintxos (tapas Basque) terbaik di Barcelona. Deretan bar dengan pintxos harga merakyat (€1-2). Wajib dicoba!",
        "neighbors": ["poble_sec"]
    },
    
    "bunkers": {
        "name": "El Bunkers - Carmel Hill",
        "category": "viewpoint",
        "description": "Bekas bunker perang sipil, sekarang spot sunset terbaik dengan view 360° Barcelona. Tempat nongkrong anak muda lokal.",
        "neighbors": ["gracia", "park_guell"]
    },
    
    "hospital_sant_pau": {
        "name": "Hospital de Sant Pau",
        "category": "historic",
        "description": "Rumah sakit bersejarah Art Nouveau karya Lluís Domènech i Montaner. Situs UNESCO yang lebih sepi dari Sagrada Familia.",
        "neighbors": ["sagrada_familia", "guinardo"]
    },
    
    "guinardo": {
        "name": "El Guinardó",
        "category": "neighborhood",
        "description": "Daerah perbukitan di utara Barcelona. View bagus, jauh dari turis, vibes lokal banget.",
        "neighbors": ["hospital_sant_pau", "bunkers"]
    },
    
    "xampanyet": {
        "name": "El Xampanyet",
        "category": "bar",
        "description": "Bar legendaris di Born sejak 1929. Spesialisasi cava (sampanye lokal) dan tapas tradisional. Selalu ramai lokal.",
        "neighbors": ["el_born", "picasso"]
    },
    
    "cal_pape": {
        "name": "Cal Pep",
        "category": "restaurant",
        "description": "Restoran seafood legendaris di Born. Antri panjang, tapi worth it. Menu tergantung catch of the day.",
        "neighbors": ["el_born", "xampanyet"]
    },
    
    "el_born": {
        "name": "El Born - Trendy Quarter",
        "category": "neighborhood",
        "description": "District trendi dengan butik desainer, bar anggur, dan restoran fusion. Jauh lebih lokal dari Gothic Quarter.",
        "neighbors": ["xampanyet", "cal_pape", "picasso"]
    }
}

def get_all_locations():
    return barcelona_locations

def get_location(location_id):
    return barcelona_locations.get(location_id)

def search_by_keyword(keyword):
    keyword = keyword.lower().strip()
    results = []
    
    for loc_id, location in barcelona_locations.items():
        if keyword in location['name'].lower():
            results.append(loc_id)
            continue
        if keyword in location['category'].lower():
            results.append(loc_id)
            continue
        if keyword in location['description'].lower():
            results.append(loc_id)
            continue

        for key, value in location.items():
            if key in ['name', 'category', 'description', 'neighbors']:
                continue
            if isinstance(value, str) and keyword in value.lower():
                results.append(loc_id)
                break
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and keyword in item.lower():
                        results.append(loc_id)
                        break
                if loc_id in results:
                    break

    return list(dict.fromkeys(results))