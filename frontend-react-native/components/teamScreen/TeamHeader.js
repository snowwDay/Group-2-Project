// Team Screen Header Component
import React from 'react'
import { StyleSheet, View, Text, Image, TouchableOpacity } from 'react-native'

// Header Component
export default function Header() {
    return(
        <View style={styles.container}>

            <TouchableOpacity>
                <Image 
                    source={{uri : 'https://img.icons8.com/ios-filled/50/ffffff/menu--v1.png'}}
                    style={styles.menu}
                />
            </TouchableOpacity>

            <Text style={styles.headerText}>My Team</Text>

        </View>
    )
}

// Team Header Style
const styles = StyleSheet.create({
    container: {
        backgroundColor: '#f56423',
        flexDirection: 'row',
        height: 60,
        shadowOpacity: .30,
        shadowRadius: 2,
        shadowOffset: {height: 1, width: 2},
    },
    menu: {
        height: 30,
        width: 30,
        marginLeft: 15,
        marginTop: 15,
    },
    headerText: {
        color: 'white',
        marginLeft: 20,
        marginTop: 18,
        fontSize: 20, 
        fontWeight: '600',
    },
}) 