# Data Barcelona - Tempat-tempat wisata Barcelona
barcelona_locations = {
    "sagrada_familia": {
        "name": "Sagrada Familia",
        "category": "landmark",
        "description": "Gereja ikonik karya Antoni Gaudi yang belum selesai. Landmark paling terkenal di Barcelona.",
        "neighbors": ["hospital_sant_pau", "gaudi_house"]
    },
    
    "park_guell": {
        "name": "Park Güell",
        "category": "park",
        "description": "Taman dengan mosaik warna-warni karya Gaudi. View bagus ke kota Barcelona.",
        "neighbors": ["gracia", "bunkers"]
    },
    
    "gracia": {
        "name": "Gràcia",
        "category": "neighborhood",
        "description": "District bohemian dengan plaza-plaza kecil dan vibe artistik.",
        "neighbors": ["park_guell", "carrer_verdi", "plaça_sol"]
    },
    
    "carrer_verdi": {
        "name": "Carrer Verdi",
        "category": "street",
        "description": "Jalan utama di Gràcia dengan bioskop indie dan tapas bar.",
        "neighbors": ["gracia", "plaça_sol"]
    },
    
    "plaça_sol": {
        "name": "Plaça del Sol",
        "category": "square",
        "description": "Plaza paling hidup di Gràcia dengan bar dan kafe outdoor.",
        "neighbors": ["gracia", "carrer_verdi"]
    },
    
    "el_raval": {
        "name": "El Raval",
        "category": "neighborhood",
        "description": "Daerah multikultural dengan restoran internasional dan seni jalanan.",
        "neighbors": ["macba", "la_rambla_del_raval", "boqueria"]
    },
    
    "macba": {
        "name": "MACBA",
        "category": "museum",
        "description": "Museum seni kontemporer dengan plaza tempat nongkrong skater.",
        "neighbors": ["el_raval", "la_rambla_del_raval"]
    },
    
    "la_rambla": {
        "name": "La Rambla",
        "category": "street",
        "description": "Jalan terkenal di Barcelona, penuh dengan pedagang kaki lima dan kafe.",
        "neighbors": ["boqueria", "placa_catalunya", "gothic_quarter"]
    },
    
    "la_rambla_del_raval": {
        "name": "Rambla del Raval",
        "category": "street",
        "description": "Jalan di Raval dengan patung kucing raksasa (El Gat).",
        "neighbors": ["el_raval", "macba"]
    },
    
    "boqueria": {
        "name": "La Boqueria",
        "category": "market",
        "description": "Pasar terkenal dengan berbagai makanan segar, jus, dan tapas.",
        "neighbors": ["la_rambla", "el_raval"]
    },
    
    "placa_catalunya": {
        "name": "Plaça de Catalunya",
        "category": "square",
        "description": "Alun-alun pusat Barcelona, pertemuan antara kota tua dan baru.",
        "neighbors": ["la_rambla", "gothic_quarter", "passeig_gracia"]
    },
    
    "passeig_gracia": {
        "name": "Passeig de Gràcia",
        "category": "street",
        "description": "Jalan mewah dengan rumah-rumah modernis dan toko-toko branded.",
        "neighbors": ["placa_catalunya", "casa_batllo", "casa_mila"]
    },
    
    "casa_batllo": {
        "name": "Casa Batlló",
        "category": "landmark",
        "description": "Rumah karya Gaudi dengan fasad bergelombang dan warna-warni.",
        "neighbors": ["passeig_gracia", "casa_mila"]
    },
    
    "bunkers": {
        "name": "El Bunkers del Carmel",
        "category": "viewpoint",
        "description": "Bekas bunker perang, spot sunset terbaik dengan view 360° Barcelona.",
        "neighbors": ["park_guell", "guinardo"]
    },
    
    "guinardo": {
        "name": "El Guinardó",
        "category": "neighborhood",
        "description": "Daerah perbukitan dengan view bagus dan vibes lokal.",
        "neighbors": ["hospital_sant_pau", "bunkers"]
    },
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
    return list(dict.fromkeys(results))
