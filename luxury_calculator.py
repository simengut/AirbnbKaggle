class SimpleLuxuryCalculator:
    def __init__(self):
        self.luxury_indicators = {
            # Basic Comfort (30% of score)
            'basic_comfort': {
                'essential': [
                    'tv', 'wifi', 'kitchen', 'air conditioning', 'heating',
                    'washer', 'dryer', 'refrigerator', 'microwave'
                ],
                'premium': [
                    'smart', 'high-speed', 'fully equipped',
                    'central air', 'laundry room'
                ]
            },
            
            # Living Space (30% of score)
            'living_space': {
                'essential': [
                    'bedroom', 'bathroom', 'living room', 'dining area',
                    'workspace', 'parking'
                ],
                'premium': [
                    'master', 'suite','walk-in',
                    'office', 'garage', 'balcony', 'patio', 'deck'
                ]
            },
            
            # Amenities (20% of score)
            'amenities': {
                'basic': [
                    'coffee', 'dishwasher', 'iron', 'hair dryer',
                    'toiletries', 'towels', 'linens'
                ],
                'premium': [
                    'pool', 'gym', 'hot tub', 'sauna', 'game room',
                    'entertainment', 'grill'
                ]
            },
            
            # Location/View Features (20% of score)
            'location_features': {
                'basic': [
                    'view', 'quiet', 'safe', 'transportation'
                ],
                'premium': [
                    'waterfront', 'beachfront', 'ocean', 'mountain',
                    'ski-in/ski-out', 'private', 'downtown'
                ]
            }
        }

    def calculate_score(self, amenities):
        amenities_text = ' '.join(str(amenity).lower() for amenity in amenities)
        
        scores = {
            'basic_comfort': 0,
            'living_space': 0,
            'amenities': 0,
            'location_features': 0
        }
        
        # Basic Comfort (30%)
        essential_count = sum(1 for item in self.luxury_indicators['basic_comfort']['essential'] 
                            if item in amenities_text)
        premium_count = sum(1 for item in self.luxury_indicators['basic_comfort']['premium'] 
                          if item in amenities_text)
        scores['basic_comfort'] = min(1.0, (essential_count * 0.15) + (premium_count * 0.1))
        
        # Living Space (30%)
        essential_count = sum(1 for item in self.luxury_indicators['living_space']['essential'] 
                            if item in amenities_text)
        premium_count = sum(1 for item in self.luxury_indicators['living_space']['premium'] 
                          if item in amenities_text)
        scores['living_space'] = min(1.0, (essential_count * 0.15) + (premium_count * 0.1))
        
        # Amenities (20%)
        basic_count = sum(1 for item in self.luxury_indicators['amenities']['basic'] 
                         if item in amenities_text)
        premium_count = sum(1 for item in self.luxury_indicators['amenities']['premium'] 
                          if item in amenities_text)
        scores['amenities'] = min(1.0, (basic_count * 0.1) + (premium_count * 0.15))
        
        # Location Features (20%)
        basic_count = sum(1 for item in self.luxury_indicators['location_features']['basic'] 
                         if item in amenities_text)
        premium_count = sum(1 for item in self.luxury_indicators['location_features']['premium'] 
                          if item in amenities_text)
        scores['location_features'] = min(1.0, (basic_count * 0.1) + (premium_count * 0.2))
        
        # Calculate final score with weights
        final_score = (
            scores['basic_comfort'] * 0.30 +
            scores['living_space'] * 0.30 +
            scores['amenities'] * 0.20 +
            scores['location_features'] * 0.20
        )
        
        return round(final_score, 2)

    def get_luxury_level(self, score):
        if score >= 0.8:
            return 5    # 'Luxury'
        elif score >= 0.6:
            return 4    # 'Premium'
        elif score >= 0.4:
            return 3    # 'Comfortable'
        elif score >= 0.2:
            return 2    # 'Basic'
        else:
            return 1    # 'Minimal'
        
def calculate_luxury_metrics(amenities_list):
    calculator = SimpleLuxuryCalculator()
    if isinstance(amenities_list, list):
        score = calculator.calculate_score(amenities_list)
        level = calculator.get_luxury_level(score)
        return {'luxury_score': score, 'luxury_level': level}
    return {'luxury_score': 0, 'luxury_level': 'Standard'}