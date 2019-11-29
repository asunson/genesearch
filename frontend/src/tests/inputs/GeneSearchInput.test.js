import React from 'react';
import {mount} from 'enzyme';

describe("GeneSearchInput", () => {
    let component;
    const handleTextChangeSpy = jest.fn();

    beforeEach(() => {
        component = mount(
            <GeneSearchInput handleTextChange={handleTextChangeSpy}/>
        )
    });

    it('should render the input bar', () => {
        expect(component.find("Paper").text()).toContain("Query for your genes of interest here:");
        
    });
});